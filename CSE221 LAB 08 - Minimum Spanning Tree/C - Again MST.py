class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        root = self.find(self.parent[i])
        self.parent[i] = root
        return root
    
    def unite(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1

def secondMST(V, edges):
    edges.sort(key=lambda a: a[2])
    dsu = DSU(V)
    mst_cost = 0
    mst_edges = []
    count = 0
    for i in range(len(edges)):
        x, y, w = edges[i]
        if dsu.find(x) != dsu.find(y):
            dsu.unite(x, y)
            mst_cost += w
            mst_edges.append(i)
            count += 1
            if count == V - 1:
                break
    if count < V - 1:
        return -1
    res = float('inf')
    for exclude_idx in mst_edges:
        dsu = DSU(V)
        new_cost = 0
        new_count = 0
        for i in range(len(edges)):
            if i == exclude_idx:
                continue
            x, y, w = edges[i]
            if dsu.find(x) != dsu.find(y):
                dsu.unite(x, y)
                new_cost += w
                new_count += 1
                if new_count == V - 1:
                    break
        if new_count == V - 1 and new_cost > mst_cost:
            res = min(res, new_cost)
    for include_idx in range(len(edges)):
        if include_idx in mst_edges:
            continue
        dsu = DSU(V)
        new_cost = 0
        new_count = 0
        x, y, w = edges[include_idx]
        dsu.unite(x, y)
        new_cost += w
        new_count += 1
        for i in range(len(edges)):
            if i == include_idx:
                continue
            x, y, w = edges[i]
            if dsu.find(x) != dsu.find(y):
                dsu.unite(x, y)
                new_cost += w
                new_count += 1
                if new_count == V - 1:
                    break
        if new_count == V - 1 and new_cost > mst_cost:
            res = min(res, new_cost)
    return res if res != float('inf') else -1

N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append([u-1, v-1, w])
print(secondMST(N, edges))