import sys
sys.setrecursionlimit(20 * 10000000 + 5)

class Node:
    def __init__(self, data):
        self.data = data
        self.colour = "White"

class adjacency_list:
    def __init__(self, n):
        self.adj = [[] for _ in range(n)]  
        self.nodes = [Node(i + 1) for i in range(n)]  
        self.subtree_size = [0] * n  

    def add_edge(self, u, v):
        self.adj[u - 1].append(v - 1) 
        self.adj[v - 1].append(u - 1)

def DFS_visit(G, u_index):
    u = G.nodes[u_index]
    u.colour = "Grey"
    G.subtree_size[u_index] = 1  

    for v_index in G.adj[u_index]:
        v = G.nodes[v_index]
        if v.colour == "White":
            DFS_visit(G, v_index)
            G.subtree_size[u_index] += G.subtree_size[v_index]  

    u.colour = "Black"

def DFS(G, root_index):
    for u in G.nodes:
        u.colour = "White"
    DFS_visit(G, root_index)


def solve():
    n, r = map(int, input().split())  
    G = adjacency_list(n)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        G.add_edge(u, v)

    DFS(G, r - 1)  

    q = int(input())
    result = []
    for _ in range(q):
        x = int(input())
        result.append(G.subtree_size[x - 1]) 
    for i in result:
        print(i)
solve()