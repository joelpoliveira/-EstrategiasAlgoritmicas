from sys import stdin, stdout
from pprint import pprint

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

def int_cubes(c):
    Ix_min = Iy_min = Iz_min = float("-inf")
    Ix_max = Iy_max = Iz_max = float("inf")

    for cube in c:
        Ix_min = max(Ix_min, cube[0])
        Iy_min = max(Iy_min, cube[1])
        Iz_min = max(Iz_min, cube[2])

        Ix_max = min(Ix_max, cube[0]+cube[3])
        Iy_max = min(Iy_max, cube[1]+cube[3])
        Iz_max = min(Iz_max, cube[2]+cube[3])
    
    return max(0, Ix_max - Ix_min) * max(0, Iy_max - Iy_min) * max(0, Iz_max - Iz_min)
        

if __name__=="__main__":
    n = int(readln())
    cubes = [list(map(int, readln().split())) for _ in range(n)]
    outln(int_cubes(cubes))
