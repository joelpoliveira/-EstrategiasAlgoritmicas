from sys import stdin, stdout

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

if __name__=='__main__':
	data = list(map(int, readln().split()))
	outln( data[0] * data[1] )