import sys
sys.setrecursionlimit(2*100000+5)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.colour = 0
 
 
class adjacency_list:
    def __init__(self, n):
        self.head = [None] * n
        self.nodes = [Node(i + 1) for i in range(n)]  
 
    def add_edge(self, u, v):
        new_node_v = Node(v)
        new_node_v.next = self.head[u - 1]
        self.head[u - 1] = new_node_v
 
        new_node_u = Node(u)
        new_node_u.next = self.head[v - 1]
        self.head[v - 1] = new_node_u
 
def DFS_visit(G, u):
    u.colour = "Grey"
    print(u.data, end = " ")
    temp = G.head[u.data - 1]
    while temp:
        v = G.nodes[temp.data - 1]
        if v.colour == "White":
            DFS_visit(G, v)
        temp = temp.next
    u.colour = "Black"
 
 
def DFS(G):
    for u in G.nodes:
        u.colour = "White"
    for u in G.nodes:
        if u.colour == "White":
            DFS_visit(G, u)
 
# ----------- INPUT ------------
n, m = map(int, input().split())
obj = adjacency_list(n)
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for i in range(m):
    
    obj.add_edge(x[i], y[i])
 
 
DFS(obj)              
