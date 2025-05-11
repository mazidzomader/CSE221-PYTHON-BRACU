import heapq

class Graph:
    def __init__(self, n):
        self.node = [[] for _ in range(n)]

    def add_edge(self, s, d, w):
        self.node[s - 1].append((d, w))

def Parity_Edges(G, N):
    dist = [[float('inf')] * N for _ in range(2)]  
    dist[0][0] = 0
    dist[1][0] = 0

    Q = []
    heapq.heappush(Q, (0, 1, -1)) 

    while Q:
        d_u, u, last_parity = heapq.heappop(Q)
        for v, w in G.node[u - 1]:
            parity = w % 2
            if parity == last_parity:
                pass
            else:
                if d_u + w < dist[parity][v - 1]:
                    dist[parity][v - 1] = d_u + w
                    heapq.heappush(Q, (dist[parity][v - 1], v, parity))

    ans = min(dist[0][N - 1], dist[1][N - 1])
    if ans == float('inf'): 
        return -1 
    return ans

def solve():
    N, M = map(int, input().split())
    G = Graph(N)
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))
    for i in range(M):
        G.add_edge(u[i], v[i], w[i])
    print(Parity_Edges(G, N))

solve()

