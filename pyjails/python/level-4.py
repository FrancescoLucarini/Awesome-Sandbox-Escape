#! /usr/bin/python3

import readline
from jail import intro

print(intro(4))

print("Welcome to your doom!!!")
print()
print("Protections:")
print("I deleted __import__ from __builtins__ (but I made a backup...)")
print("eval() instad of exec()")
print()

suspicious = __builtins__.__import__

del __builtins__.__import__

while True:
    try:
        cmd = input(">>> ")
        print(eval(cmd))
    except EOFError:
        exit()
    except Exception as e:
        print("Error ", e)
