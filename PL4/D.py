from sys import stdin, stdout
from time import time

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

def path(n, v, p):
    
    for i in range(1,n):
        for j in range(n):
            if j>i:
                break
            v[i][j] = max(v[i-1][j-1], v[i-1][j]) + p[i][j]
    return max(v[n-1])


if __name__=="__main__":
    start = time()
    for _ in range(int(readln())):
        n = int(input())
        v = [[0 for j in range(n)] for i in range(n)]
        p = [ list(map(int, readln().split())) + [0]*(n-i- 1) for i in range(n) ]
        v[0][0] = p[0][0]
        outln(path(n, v, p))
    outln(time()-start)