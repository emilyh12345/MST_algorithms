# CSCI 220/620
# Summer 2022
# Assignment 8-MST Algorithms
# Emily Haller
# Prim from https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
# Kruskal from https://www.geeksforgeeks.org/kruskals-algorithm-simple-implementation-for-adjacency-matrix/
import random


def random_graph(size, max_cost):
    a = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(i+1, size):
            a[i][j] = random.randint(1, max_cost)
            a[j][i] = a[i][j] # make symmetric / undirected which will be same over diagonal
    return a


def min_key(keys, visited): # find smallest key not yet visited
    min_value = 1000000
    min_index = -1
    for v in range(len(keys)):
        if keys[v] < min_value and not visited[v]:
            min_value = keys[v]
            min_index = v
    return min_index


# Prims algorithm
def print_mst(graph, parents):
    print("Prims MST: ")
    total_weight = 0
    print("Edge \t     Weight")
    for i in range(1, len(parents)):
        weight = graph[i][parents[i]]
        total_weight += weight
        print(parents[i], "-", i, ":", "\t", weight)
    print("Total weight: ", total_weight)


def prim_mst(graph):
    n = len(graph)
    keys = [1000000] * n
    parents = [-1] * n
    keys[0] = 0
    visited = [False] * n
    parents[0] = -1
    edge_count_prim = 0
    while edge_count_prim < n - 1:
        for i in range(n):
            u = min_key(keys, visited)
            visited[u] = True
            for v in range(n):
                if not visited[v] and keys[v] > graph[u][v] > 0:
                    keys[v] = graph[u][v]
                    parents[v] = u
        edge_count_prim += 1
    print_mst(graph, parents)
    print("Total edges: ", edge_count_prim)
    print("total vertices: ", edge_count_prim + 1)
    print()


# Kruskals algorithm
def kruskal_find(parents, i):
    while parents[i] != i:
        i = parents[i]
    return i


def kruskal_union(parents, i, j):
    a = kruskal_find(parents, i)
    b = kruskal_find(parents, j)
    parents[a] = b


def kruskal_mst(graph):
    print("Kruskal MST: ")
    total_weight = 0
    n = len(graph)
    parents = [i for i in range(n)]
    edge_count = 0
    while edge_count < n - 1:
        min_edge = 1000000
        a = -1
        b = -1
        for i in range(n):
            for j in range(n):
                if min_edge > graph[i][j] > 0 and kruskal_find(parents, i) != kruskal_find(parents, j):
                    min_edge = graph[i][j]
                    a = i
                    b = j
        kruskal_union(parents, a, b)
        print(a, '-', b, ":", "\t", graph[a][b])
        edge_count += 1
        total_weight += min_edge
    print("Total weight: ", total_weight)
    print("Total edges: ", edge_count)
    print("Total vertices: ", edge_count + 1)
    print()


def print_adj_matrix(a):
    print("\t", end="")
    for j in range(len(a)):
        print(str(j) + "\t", end="")
    print()
    for i in range(len(a)):
        row = a[i]
        print(str(i) + ":\t", end="")
        for col in row:
            print(str(col) + "\t", end="")
        print()
    print()


def main():
    a = random_graph(10, 1000)
    print_adj_matrix(a)
    prim_mst(a)
    kruskal_mst(a)
    print()
    b = random_graph(20, 1000)
    print_adj_matrix(b)
    prim_mst(b)
    kruskal_mst(b)


if __name__ == "__main__":
    main()