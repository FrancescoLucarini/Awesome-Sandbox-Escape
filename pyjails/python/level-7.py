#! /usr/bin/python3

import readline
import re
from jail import intro

print(intro(7))

print("Welcome to your doom!!!")
print()
print("Protections:")
print("I do not like strings. You may not type \" or '")
print("eval() instead of exec()")
print() 

while True:
    try:
        cmd = input(">>> ")
        if '"' in cmd or "'" in cmd:
            print("NO!")
        else:
            print(eval(cmd))
    except EOFError:
        exit()
    except Exception as e:
        print("Error ", e)
