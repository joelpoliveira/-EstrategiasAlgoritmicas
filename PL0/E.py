from sys import stdin, stdout
from collections import deque

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

if __name__ == '__main__':

	for line in range(int(readln())):
		stack = []
		for elem in readln().split():
			if elem == '+':
				d2 = stack.pop()
				d1 = stack.pop()
				stack.append(d1 + d2)
			
			elif elem == '-':	
				d2 = stack.pop()
				d1 = stack.pop()
				stack.append(d1 - d2)

			else:
				stack.append(int(elem))
		outln(stack[0])
			