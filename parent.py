import os
import time
import subprocess
import sys

if __name__ == "__main__":
	print(f'Parent PID: {os.getpid()}')
	try:
		subprocess.Popen(["python", "child.py"], stdin=subprocess.PIPE)
	
	except e:
		print(f"Couldn't open child.py: {e}")

	time.sleep(10)
	
