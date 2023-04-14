#! /usr/bin/python3

import readline
import re
from jail import intro

import os

def escape(key):
    if key == "swordfish":
        os.system("sh")
    else:
        print("NOPE!")

del os

print(intro(8))

print("Welcome to your doom!!!")
print()
print("Protections:")
print("I'll let you out if you call escape() with the key!")
print()

while True:
    try:
        cmd = input(">>> ")
        print(eval(cmd))
    except EOFError:
        exit()
    except Exception as e:
        print("Error ", e)
