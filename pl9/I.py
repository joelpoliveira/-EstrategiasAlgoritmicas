from sys import stdin, stdout
from pprint import pprint

d = []
q = []
MAX_NUMBER = 65536

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

def dikstra(g, s, t):
    d[s] = 0
    #print(t)
    #pprint(g)

    for _ in range(len(q)-1):
        for u in q:
            for v in range(n):
                if g[u][v]!=-1 and v!=u:
                    if d[v] > d[u] + g[u][v]:
                        d[v] = d[u] + g[u][v]
    return d[t]
    

if __name__=="__main__":
    n, last = list(map(int, readln().split()))
    last-=1
    weights = [0 for _ in range(n)]
    for i in range(n):
        line = list(map(int, readln().split()))
        weights[line[0] - 1] = line[1:]
        q.append(i)
        d.append(MAX_NUMBER)

    outln(dikstra(weights, 0, last))