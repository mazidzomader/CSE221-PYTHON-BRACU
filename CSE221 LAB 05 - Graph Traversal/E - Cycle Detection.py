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

def DFS_visit(G, u):
    u.colour = "Grey"
    temp = G.head[u.data - 1]
    while temp:
        v = G.nodes[temp.data - 1]
        if v.colour == "White":
            DFS_visit(G, v)
        if v.colour == "Grey":
            return True
        temp = temp.next
    u.colour = "Black"
    

def DFS(G):
    for u in G.nodes:
        u.colour = "White"
    for u in G.nodes:
        if u.colour == "White":
            X = DFS_visit(G, u)
            if X == True:
                print ("YES")
                return
    print("NO")

# ----------- INPUT ------------
n, m = map(int, input().split())
obj = adjacency_list(n)

for i in range(m):
    x , y = map(int, input().split())
    obj.add_edge(x, y)
 
 
DFS(obj)              
