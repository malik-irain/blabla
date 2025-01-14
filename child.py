import os
import time
import subprocess
import sys

if __name__ == "__main__":
	print(f'Child\'s parent PID: {os.getppid()}')
	try:
		sys.stdin.read()
		time.sleep(10)
		print(f'Child\'s parent PID: {os.getppid()}')
	except e:
		print(f"Couldn't wait parent: {e}")

	print("Parent done")
	# can start