import time

now = time.time()
future = now + 10
while time.time() < future:
	print('running')
	time.sleep(1)
