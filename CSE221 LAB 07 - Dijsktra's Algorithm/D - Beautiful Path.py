import heapq

def add_edge(G, u, v):
    G[u - 1].append(v - 1)

def Beautiful_path(G, N, weights, S, D ):
    dist = [float('inf')] * N
    dist[S - 1] = weights[S - 1] 

    temp = [(weights[S - 1], S - 1)]

    while temp:
        weight_u, u = heapq.heappop(temp)
        if weight_u > dist[u]:
            continue  

        for v in G[u]:
            new_cost = weight_u + weights[v]
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(temp, (new_cost, v))
    return dist
def solve():
    
    N, M, S, D = map(int, input().split())
    weights = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        add_edge(G, u, v)    
    
    result = Beautiful_path(G, N, weights, S, D)
    if result[D - 1] == float('inf'):
        print(-1)
    else:
        print(result[D - 1])
solve()
