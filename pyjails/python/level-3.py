#! /usr/bin/python3

import readline
from jail import intro

print(intro(3))

print("Welcome to your doom!!!")
print()
print("Protections:")
print("eval() instead of exec()")
print("You can't say \"import\" at all!")
print()

while True:
    try:
        cmd = input(">>> ")
        if "import" in cmd:
            print("NO!")
        else:
            print(eval(cmd))
    except EOFError:
        exit()
    except Exception as e:
        print("Error ", e)
