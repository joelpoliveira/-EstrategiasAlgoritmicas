from sys import stdin, stdout
from pprint import pprint
from itertools import combinations

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

dfs = []
low = []
parent = []
edges = []
aps = set()
t = 1

def ap(v):
    global t
    low[v] = dfs[v] = t
    t+=1
    for edge in list(filter(lambda edge: v in edge, edges) ):
        w = edge[0] if edge[0] != v else edge[1]
        if dfs[w] == -1:
            parent[w] = v
            ap(w)
            if dfs[v]==1 and dfs[w]!=2:
                aps.add(v)
            elif dfs[v]!=1 and low[w]>=dfs[v]:
                aps.add(v)
        elif parent[v]!=w:
            low[v] = min(low[v], dfs[w])

if __name__=="__main__":
    while True:
        n = int(readln())
        if n==0:
            break
        else:

            edges = []
            while True:
                line=readln()
                if line=="0":
                    break

                vertices = list(map(int, line.split()))
                edges += list(map(lambda edge: (vertices[0] - 1, edge - 1), vertices[1:]))

            dfs = [-1 for _ in range(n)]
            low = [-1 for _ in range(n)]
            parent = [-1 for _ in range(n)]
            aps=set()
            
            t = 1
            ap(0)
            #pprint(aps)
            outln(len(aps))