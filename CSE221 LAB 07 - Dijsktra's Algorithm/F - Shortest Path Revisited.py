import heapq

class Graph:
    def __init__(self, n):
        self.node = [[] for _ in range(n)]
    
    def add_edge(self, u, v, w):
        self.node[u - 1].append((v, w))
        self.node[v - 1].append((u, w)) 

def second_shortest_path(G, S, D, N):
    dist = [[float('inf'), float('inf')] for _ in range(N)]
    dist[S - 1][0] = 0
    
    temp = []
    heapq.heappush(temp, (0, S))

    while temp:
        d_u, u = heapq.heappop(temp)
        
        if d_u > dist[u - 1][1]:  
            continue

        for v, w in G.node[u - 1]:
            new_dist = d_u + w
            if new_dist < dist[v - 1][0]:
                dist[v - 1][1] = dist[v - 1][0]  
                dist[v - 1][0] = new_dist  
                heapq.heappush(temp, (new_dist, v))
            elif dist[v - 1][0] < new_dist and new_dist < dist[v - 1][1]:
                dist[v - 1][1] = new_dist
                heapq.heappush(temp, (new_dist, v))

    
    if dist[D - 1][1] == float('inf'):
        return -1 
    return dist[D - 1][1]

def solve():
    N, M, S, D = map(int, input().split())
    G = Graph(N)
    for _ in range(M):
        u, v, w = map(int, input().split())
        G.add_edge(u, v, w)
    
    print(second_shortest_path(G, S, D, N))

solve()
