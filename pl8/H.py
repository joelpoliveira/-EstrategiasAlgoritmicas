from sys import stdin, stdout
from collections import deque
marks = None
graph = None

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

def connections(v):
    q = deque()
    marks[0] = 1
    q.append(0)

    while q:
        t = q.popleft()
        for edge in graph[t]:
            if marks[edge] == -1:
                marks[edge] = 1 - marks[t]
                q.append(edge)
            elif marks[edge] == marks[t]:
                return "NO"

    return "NOT SURE"

if __name__ == '__main__':

    while True:
        try:
            n, m = list(map(int, readln().split()))
        except:
            break
        marks = [-1 for i in range(n)]
        graph = [[] for i in range(n)]

        for i in range(m):
            p1,p2 = list(map(int, readln().split()))
            graph[p1-1].append(p2-1)
            graph[p2-1].append(p1-1)

        outln(connections(0))

