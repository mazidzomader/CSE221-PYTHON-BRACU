import heapq

class Graph:
    def __init__(self, n):
        self.node = [[] for _ in range(n)]  

    def add_edge(self, s, d, w):
        self.node[s - 1].append((d, w))  

def Dijsktra(G, S, D, N):
    dist = [float('inf')] * N
    prev = [None] * N
    dist[S - 1] = 0
    Q = []
    heapq.heappush(Q, (0, S))

    while Q:
        d_u, u = heapq.heappop(Q)
        if d_u > dist[u - 1]:
            continue
        for v, w in G.node[u - 1]:
            if dist[u - 1] + w < dist[v - 1]:
                dist[v - 1] = dist[u - 1] + w
                prev[v - 1] = u
                heapq.heappush(Q, (dist[v - 1], v))

    if dist[D - 1] == float('inf'):
        return -1, []

    path = []
    u = D
    while u is not None:
        path.append(u)
        u = prev[u - 1]
    path.reverse()
    return dist[D - 1], path

def solve():
    import sys
    input = sys.stdin.readline
    N, M, S, D = map(int, input().split())
    G = Graph(N)
    Edge_Source = list(map(int, input().split()))
    Edge_Destini = list(map(int, input().split()))
    Edge_Weight = list(map(int, input().split()))
    for idx in range(M):
        G.add_edge(Edge_Source[idx], Edge_Destini[idx], Edge_Weight[idx])
    Distance, Path = Dijsktra(G, S, D, N)
    if Distance == -1:
        print(-1)
    else:
        print(Distance)
        print(" ".join(map(str, Path)))
        
solve()
