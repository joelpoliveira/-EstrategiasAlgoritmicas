from sys import stdin, stdout
import ctypes

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

if __name__=='__main__':
    for _ in range(int(readln())):
        n, m = list(map(int, readln().split()))

        p = sorted([int(readln()) for i in range(n)])

        g_count = 1
        g = p[0] + m
        for i in range(1,n):
            if p[i] > g + m:
                g = p[i] + m
                g_count+=1
        
        outln(g_count)
    