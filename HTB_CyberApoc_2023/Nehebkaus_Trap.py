#!/usr/bin/env python3
import sys
import time

BLACKLIST = ('.', '_', '/', '"', ';', ' ', "'", ',')

class Color:
  WHITE = '\033[37m'
  RED = '\033[31m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  BOLD = '\033[1m'

def _print(s):
  for c in list(s):
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.015)

def banner():
  print(f'{Color.RED}{Color.BOLD}'
        '    __\n'
        '   {00}\n'
        '   \__/\n'
        '   /^/\n'
        '  ( (\n' 
        '   \_\_____\n'
        '   (_______)\n'
        '  (_________()Ooo.')

  _print(f'{Color.BLUE}\n'
         "[ Nehebkau's Trap ]\n"
         f'{Color.WHITE}\n'
         'You are trapped!\n'
         'Can you escape?\n')

def loop():
  inp = input('> ')
  banned = [c for c in BLACKLIST if c in inp]
  if len(banned):
    print(f'\n{Color.RED}[!] Blacklisted character(s): {banned}{Color.WHITE}\n')
    return
  print('\n[*] Input accepted!\n')
  try: eval(inp)
  except Exception as e: print(f'Error: {e}\n')

if __name__ == '__main__':
  banner()
  for _ in range(10): loop()
  print(f'{Color.RED}[!] The walls crush you!')
