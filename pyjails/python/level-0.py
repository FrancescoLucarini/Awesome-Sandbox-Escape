#! /usr/bin/python3

import readline
from jail import intro

print(intro(0))

print("Welcome to your doom!!!")
print()
print("Protections:")
print("None")
print()

while True:
    try:
        exec(input(">>> "))
    except EOFError:
        exit()
    except Exception as e:
        print("Error ", e)
