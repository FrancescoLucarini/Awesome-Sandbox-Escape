#! /usr/bin/python3

import readline
from jail import intro

print(intro(1))

print("Welcome to your doom!!!")
print()
print("Protections:")
print("eval() instead of exec()")
print()

while True:
    try:
        print(eval(input(">>> ")))
    except EOFError:
        exit()
    except Exception as e:
        print("Error ", e)
