from sys import stdin, stdout

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

best = 999999
n = 0
nlig = []
cost = []
visited = []

def net(v , c ):
    global best

    if c >= best:
        return
    if v==n:
        best = c
        return
    for i in range(n):
        if visit[i] and nlig[i]<k:
            for j in range(n):
                if not visit[j]:
                    if cost[i][j]>0:
                        nlig[i]+=1
                        nlig[j]+=1
                        visit[j] = 1

                        net(v+1, c + cost[i][j])

                        visit[j] = 0
                        nlig[j]-=1
                        nlig[i]-=1

if __name__ == "__main__":
    while True:
        try:
            n,m,k = list(map(int, readln().split()))
        except:
            break
        best = 999999
        cost = [[0 for i in range(n)] for j in range(n)]
        nlig = [0 for i in range(n)]
        visit = [0 for i in range(n)]
        visit[0] = 1
        
        for i in range(m):
            id1,id2,c = list(map(int, readln().split()))
            cost[id1 - 1][id2 - 1] = c
            cost[id2 - 1][id1 - 1] = c
        net(1, 0)

        if best!=999999:
            outln(best)
        else:
            outln("NO WAY!")
