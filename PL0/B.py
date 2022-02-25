from sys import stdin, stdout

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

if __name__=='__main__':
	readln()
	data = list(readln().split())[::-1]
	data = ' '.join(data)
	outln( data )