import os
import time
import subprocess
import sys

def main():
	print(sys.argv)
	try:
		os.remove(sys.argv[0])
	except FileNotFoundError:
		pass
		
	print(f'Parent PID: {os.getpid()}')
	try:
		subprocess.Popen(["python", "child.py"], stdin=subprocess.PIPE)
	
	except e:
		print(f"Couldn't open child.py: {e}")

	time.sleep(10)
	

if __name__ == "__main__":
	main()
