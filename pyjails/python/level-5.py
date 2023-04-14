#! /usr/bin/python3

import readline
from jail import intro

print(intro(5))

print("Welcome to your doom!!!")
print()
print("Protections:")
print("I deleted __import__ from __builtins__ (but I made a backup...)")
print("You're not allowed to say \"vars\", \"locals\", or \"globals\"")
print("eval() instad of exec()")
print()

what_a_weird_variable = __builtins__.__import__

del __builtins__.__import__

while True:
    try:
        cmd = input(">>> ")
        if "vars" in cmd.lower() or "locals" in cmd.lower() or "globals" in cmd.lower():
            print("NO!")
        else:
            print(eval(cmd))
    except EOFError:
        exit()
    except Exception as e:
        print("Error ", e)
