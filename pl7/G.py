from sys import stdin, stdout
from pprint import pprint

best=None
graph=None
neighbor=None

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

def mis(node_i, size, n):
    
    global best
    if (size > best):
        best = size
    
    ub = 0
    for i in range(node_i+1,n):
        if neighbor[i]==0:
            ub+=1
            
    if ub+size <= best:
        return

    for i in range(node_i+1,n):
        if graph[node_i][i]==1:
            neighbor[i] += 1

    for i in range(node_i+1, n):
        if neighbor[i]==0:
            #print(neighbor)
            mis(i, size+1, n)

    for i in range(node_i+1,n):
        if graph[node_i][i]==1:
            neighbor[i] -= 1


if __name__=="__main__":
    while True:
        try:
            n,m=list(map(int, readln().split()))
        except:
            break

        best=0
        graph = [[0 for _ in range(n)] for _ in range(n)]
        neighbor = [0 for _ in range(n)]
        for _ in range(m):
            x,y=list(map(int, readln().split()))
            graph[x][y] = graph[y][x] = 1
        
        for i in range(n):
            #print("#"*5, f"next_trial {i}", "#"*5, "\n\n")
            mis(i, 0, n)
            
        outln(best + 1)
        
