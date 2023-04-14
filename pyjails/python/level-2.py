#! /usr/bin/python3

import readline
from jail import intro

print(intro(2))

print("Welcome to your doom!!!")
print()
print("Protections:")
print("You can't start a line with \"import\" (after stripping whitespace)")
print()

while True:
    try:
        cmd = input(">>> ")
        if "import" == cmd.strip()[0:6]:
            print("NO!")
        else:
            print(exec(cmd))
    except EOFError:
        exit()
    except Exception as e:
        print("Error ", e)
