parent = {}
rank = {}

def MakeSet(v):
    parent[v] = v
    rank[v] = 0

def Find(v):
    if parent[v] != v:
        parent[v] = Find(parent[v])
    return parent[v]

def Union(u, v):
    root_u = Find(u)
    root_v = Find(v)

    if root_u == root_v:
        return False

    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True



n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))  

edges.sort()  

for i in range(1, n + 1):
    MakeSet(i)

total_cost = 0

for w, u, v in edges:
    if Union(u, v):
        total_cost += w

print(total_cost)
