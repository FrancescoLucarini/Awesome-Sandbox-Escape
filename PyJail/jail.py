#!/usr/bin/python3
blacklist = ['write','open','pty','from','sys','platform','type', 'ls', 'cat', 'flag', 'head', 'tail']
import os

while True:
	cmd = input(">>> ")
	if any([x in cmd  for x in blacklist]):
		print ("did not pass filter")
		pass
	else:
		try:
			print(cmd)
			exec(cmd)
		except Exception as e :
			print(f"error running command\n{e}")
			pass
