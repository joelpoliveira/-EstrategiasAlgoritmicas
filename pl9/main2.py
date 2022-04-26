from sys import stdin, stdout
from pprint import pprint

# from time import time


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n) + "\n")


# Bellman-Ford algorithm
def shortest_path(graph, n, end_node):
    distance = [float("inf") for _ in range(n)]  # Set distance to all nodes as infinite
    distance[0] = 0  # Set start node distance to itself -> 0

    edges = len(graph)  # number of edges

    for i in range(n - 1):
        for j in range(edges):
            if distance[graph[j][0]] + graph[j][2] < distance[graph[j][1]]:
                distance[graph[j][1]] = distance[graph[j][0]] + graph[j][2]

    outln(distance[end_node])


if __name__ == "__main__":
    # start = time()
    # outln(time() - start)

    n, end = list(map(int, readln().split()))
    n -= 1
    end -= 1

    graph = []

    for _ in range(n + 1):
        aux = list(map(int, readln().split()))
        x = aux[0] - 1
        aux = aux[1:]
        # print(aux)
        for i in range(len(aux)):
            if aux[i] != -1:
                graph.append([x, i, aux[i]])

    # pprint(graph)

    shortest_path(graph, n + 1, end)
