from sys import stdin, stdout

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

if __name__=='__main__':

	data = []
	while True:
		s = readln()
		if s:
			data.append(int(s))
		else:
			break

	data.sort()

	for i in data:
		outln(i)