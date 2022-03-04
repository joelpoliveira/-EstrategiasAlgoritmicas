from sys import stdin, stdout

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

board = [[False for __ in range(401)] for _ in range(401)]
cache = {}

def count(x, y, steps_left):
    if steps_left < 0:
        return 0
    if cache.get((x,y), -1) >= steps_left:
        return 0

    v=0
    if board[x+200][y+200] == False:
        board[x+200][y+200] = True
        v=1
        
    cache[(x,y)] = steps_left
    return v + count( x+2, y-1, steps_left - 1) + count( x+2, y+1, steps_left - 1) + count( x+1, y+2, steps_left - 1) + count( x-1, y+2, steps_left - 1)+count( x-2, y+1, steps_left - 1) + count( x-2, y-1, steps_left - 1) + count( x-1, y-2, steps_left - 1) + count( x+1, y-2, steps_left - 1) 

if __name__ == "__main__":
    readln()
    data = list( map( lambda line: list( map( int, line.split() )) , read_all() ) )

    counter = 0
    for line in data:
        x,y,steps = line
        counter += count( x, y, steps )
    outln(counter)