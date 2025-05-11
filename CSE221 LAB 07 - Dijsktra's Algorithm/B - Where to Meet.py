from queue import PriorityQueue
import sys

class Graph:
    def __init__(self, n):
        self.node = [[] for _ in range(n)]

    def add_edge(self, s, d, w):
        self.node[s - 1].append((d, w))  

def Dijkstra(G, S, N):
    dist = [float('inf')] * N
    prev = [None] * N
    dist[S - 1] = 0
    Q = PriorityQueue()
    Q.put((0, S)) 
    while not Q.empty():
        d_u, u = Q.get()
        if d_u > dist[u - 1]:
            continue
        for v, w in G.node[u - 1]:
            if dist[u - 1] + w < dist[v - 1]:
                dist[v - 1] = dist[u - 1] + w
                prev[v - 1] = u
                Q.put((dist[v - 1], v))
    return dist, prev

def solve():
    input = sys.stdin.readline
    N, M, S, T = map(int, input().split())
    G = Graph(N)

    for _ in range(M):
        X, Y, Z = map(int, input().split())
        G.add_edge(X, Y, Z)

    Alice_Distance, _ = Dijkstra(G, S, N)
    Bob_Distance, _ = Dijkstra(G, T, N)

    min_time = float('inf')
    meet_node = -1

    for idx in range(N):
        if Alice_Distance[idx] == float('inf') or Bob_Distance[idx] == float('inf'):
            continue
        meet = max(Alice_Distance[idx], Bob_Distance[idx])
        if meet < min_time or (meet == min_time and idx + 1 < meet_node):
            min_time = meet
            meet_node = idx + 1

    if meet_node == -1:
        print(-1)
    else:
        print(f"{min_time} {meet_node}")
solve()