import sys
sys.setrecursionlimit(20 * 10000000 + 5)
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.visited = False
        self.color = "White"
class adjacency_list:
    def __init__(self, n):
        self.head = [None] * n
        self.nodes = [Node(i + 1) for i in range(n)]  
 
    def add_edge(self, u, v):
        new_node_v = Node(v)
        new_node_v.next = self.head[u - 1]
        self.head[u - 1] = new_node_v 

def TopoSort(G):
    L = None
    for u in G.nodes:
        if not u.visited:
            L = DFS(G, u, L)
    return L
def DFS(G, u, L):
    u.visited = True
    temp = G.head[u.data - 1]  
    while temp:                
        v = G.nodes[temp.data - 1] 
        if not v.visited:
            L = DFS(G, v, L)       
        temp = temp.next
    L = Node(u.data, L)
    
    return L
def cycle_detector(G):
    for u in G.nodes:
        if u.color == "White":
            temp = DFS_cycle(G, u)
            if temp:
                return True
    return False
def DFS_cycle(G, u):
    u.color = "Gray"
    temp = G.head[u.data - 1]
    while temp:
        v = G.nodes[temp.data - 1]
        if v.color == "White":
            if DFS_cycle(G, v):  
                return True
        elif v.color == "Gray":
            return True 
        temp = temp.next
    u.color = "Black"
    return False
def solve():
    n, m = map(int, input().split())
    G = adjacency_list(n)
    for _ in range(m):
        u, v = map(int, input().split())
        G.add_edge(u, v)
    if cycle_detector(G):
        print(-1)
    else:   
        L = TopoSort(G)
        while L:
            print(L.data, end=' ')
            L = L.next
solve()
