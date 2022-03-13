from sys import stdin, stdout
from time import time


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def path(n, v, p):
    for i in range(n):
        for j in range(n):
            v[i][j] = max(v[i - 1][j - 1], v[i - 1][j]) + p[i][j]

    return max(v[-1])


if __name__ == "__main__":
    start = time()

    for _ in range(int(readln())):  # number of test cases
        n = int(readln()) # number of rows
        v = [[0 for _ in range(n)] for __ in range(n)]
        p = []
        temp = []

        for i in range(n):  # number of rows of the triangle
            temp = list(map(int, readln().split()))
            p.append(temp + [0 for _ in range(n - i - 1)])

        #print(p)

        outln(path(n, v, p))
        #outln(path(n-1, n-1, v, p))
        

    outln(time() - start)