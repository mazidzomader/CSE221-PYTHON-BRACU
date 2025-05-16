parent = {}
rank = {}
size = {}
result  = []
def MakeSet(v):
    parent[v] = v
    rank[v] = 0
    size[v] = 1

def Find(v):
    if parent[v] != v:
        parent[v] = Find(parent[v])  
    return parent[v]

def Union(u, v):
    root_u = Find(u)
    root_v = Find(v)

    if root_u == root_v:
        result.append(size[root_u])
        return

    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
        size[root_v] += size[root_u]
        result.append(size[root_v])
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
        size[root_u] += size[root_v]
        result.append(size[root_u])
    else:
        parent[root_v] = root_u
        rank[root_u] += 1
        size[root_u] += size[root_v]
        result.append(size[root_u])

n, k = map(int, input().split())
for i in range(1, n + 1):
    MakeSet(i)

for _ in range(k):
    a, b = map(int, input().split())
    Union(a, b)

for i in result:
    print(i)