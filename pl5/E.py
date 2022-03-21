from sys import stdin, stdout
from turtle import tiltangle

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

def ze_manel_das_pizzas(n,T, ts):
    half_t = int(T//2)

    dp = [ [0 if j != 0 else 1 for j in range(half_t+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(half_t+1):
            if ts[i]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-ts[i]]
    
    for i in range(half_t, -1, -1):
        if dp[n][i] == 1:
            c = i
            break
    
    i = n
    
    total=0
    while i != 0:
        if dp[i - 1][c] == 0:
            total+=ts[i]
            c = c - ts[i]
        i-=1

    #print(T, total)
    return abs(total - (T - total))
    

if __name__=='__main__':
    while True:
        try:
            n = int(readln())
        except:
            break
        ts = { i : int(readln()) for i in range(1,n+1) }
        ts.update({0:0})
        T = sum(ts.values())
        print(ze_manel_das_pizzas(n, T, ts))
