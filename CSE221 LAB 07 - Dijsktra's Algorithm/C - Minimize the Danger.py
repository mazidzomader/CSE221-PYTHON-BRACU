import heapq

class Graph:
    def __init__(self, n):
        self.node = [[] for _ in range(n)]  

    def add_edge(self, s, d, w):
        self.node[s - 1].append((d, w))  
        self.node[d - 1].append((s, w))  

def Dijkstra(G, S, N):
    dist = [float('inf')] * N
    dist[S - 1] = 0
    Q = []
    heapq.heappush(Q, (0, S))

    while Q:
        temp_u, u = heapq.heappop(Q)
        if temp_u > dist[u - 1]:
            continue
        for v, w in G.node[u - 1]:
            temp_v = max(temp_u, w)
            if temp_v < dist[v - 1]:
                dist[v - 1] = temp_v
                heapq.heappush(Q, (temp_v, v))

    return dist

def solve():
    N, M = map(int, input().split())
    G = Graph(N)

    for _ in range(M):
        X, Y, Z = map(int, input().split())
        G.add_edge(X, Y, Z)

    dist = Dijkstra(G, 1, N)
    for i in range(N):
        if dist[i] == float('inf'):
            print(-1, end=' ')
        else:
            print(dist[i], end=' ')
    print()
solve()