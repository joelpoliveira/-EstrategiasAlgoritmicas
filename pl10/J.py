from sys import stdin, stdout
from math import sqrt
from itertools import combinations
from pprint import pprint

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

set = []
rank = []
edges = []

def make_set(n):
    global set, rank
    set = [i for i in range(n)]
    rank = [0 for _ in range(n)]

def find(a):
    if set[a]!=a:
        set[a] = find(set[a])
    return set[a]

def link(a,b):
    if rank[a]>rank[b]:
        set[b] = a
    else:
        set[a] = b
    
    if rank[a] == rank[b]:
        rank[b]+=1

def union(a,b):
    link(find(a), find(b))

def kruskal(n):
    added = 0

    edges.sort(key = lambda edge: edge[0])
    for edge in edges:
        
        if (find(edge[1])!=find(edge[2])):
            union(edge[1], edge[2])
            added += edge[0]
    return added

def euc(a,b):
    return sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )

if __name__=="__main__":
    while True:
        try:
            n = int(readln())
            make_set(n)
            edges = []
            pos = {}
             
            for i in range(n):
                x,y = list(map(int, readln().split()))
                pos[i] = (x,y)
            for edge in combinations(pos.keys(), 2):
                a,b = edge
                edges.append((euc(pos[a],pos[b]), a, b))

            m = int(readln())
            for i in range(m):
                a,b = list(map(int, readln().split()))
                union(a-1, b-1)
            
            outln(f"{kruskal(n):.2f}")

        except Exception as e:
            #print(e)
            break