#! /usr/bin/python3

import readline
from jail import intro

print(intro(666))

print("Welcome to your doom!!!")
print()
print("Protections:")
print("I deleted EVERYTHING in __builtins__")
print("Input must be EXACTLY 32 characters long (excluding the newline, after stripping)")
print("You can't say \"exec\"")
print()

input = input
EOFError = EOFError
Exception = Exception
exit = exit
print = print
exec = exec
killer = delattr
for x in list(__builtins__.__dict__):
    killer(__builtins__, x)

del killer
__builtins__ = {}

while True:
    try:
        cmd = input(">>> ")
        if "exec" in cmd:
            print("NO!")
        elif cmd.strip().__len__() != 32:
            print("That wasn't exactly 32 characters")
        else:
            print(exec(cmd.strip()))
    except EOFError:
        exit()
    except Exception as e:
        print(e.__class__, e)
