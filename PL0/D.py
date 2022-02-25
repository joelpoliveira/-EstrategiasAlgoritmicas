from sys import stdin, stdout
from collections import deque

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

if __name__ == '__main__':
	
	lstack = []
	rstack = deque()
	now = '0'

	instructions = list(map(lambda line: line.strip("\n\r "), read_all()))
	for line in instructions:
		i = line.split()
		if i[0] == "MOVE":
			if i[1] == "RIGHT":
				lstack.append(now)
				now = rstack.popleft()
			else:
				rstack.appendleft(now)
				now = lstack.pop()
		else:
			if i[1] == "RIGHT":
				rstack.appendleft(i[2])
			else:
				lstack.append(i[2])
	outln('\n'.join(lstack + [now] + list(rstack)))