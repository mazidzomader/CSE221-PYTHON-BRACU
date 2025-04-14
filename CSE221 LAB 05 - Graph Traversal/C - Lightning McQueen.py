class Node:
    def __init__(self, data):
        self.data = data
        self.colour = 0
        self.parent = None
 
class adjacency_list:
    def __init__(self, n):
        self.adj = [[] for _ in range(n)]
        self.nodes = [Node(i + 1) for i in range(n)]  
 
    def add_edge(self, u, v):
        self.adj[u - 1].append(v)
        self.adj[v - 1].append(u)
 
    def sort_adj(self):
        for neighbors in self.adj:
            neighbors.sort()
class Queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []
 
    def is_empty(self):
        return not self.inbox and not self.outbox
 
    def enqueue(self, item):
        self.inbox.append(item)
 
    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        if self.outbox:
            return self.outbox.pop()
        raise IndexError("Dequeue from empty queue")
 
def bfs(G, start_node):
    for node in G.nodes:
        node.colour = 0
        node.parent = None
 
    Q = Queue()
    start_node.colour = 1
    Q.enqueue(start_node)
 
    while not Q.is_empty():
        u = Q.dequeue()
        for neighbor_data in G.adj[u.data - 1]:
            v = G.nodes[neighbor_data - 1]
            if v.colour == 0:
                v.colour = 1
                v.parent = u
                Q.enqueue(v)
 
def path_finder(D):
    path = []
    while D is not None:
        path.append(D.data)
        D = D.parent
    path.reverse()
    return path
 

n, m, s, d = map(int, input().split())
obj = adjacency_list(n)
 
x = list(map(int, input().split()))
y = list(map(int, input().split()))
 
for i in range(m):
    obj.add_edge(x[i], y[i])
 
obj.sort_adj()  
 
bfs(obj, obj.nodes[s - 1])
path = path_finder(obj.nodes[d - 1])
 
if obj.nodes[d - 1].colour == 0:
    print(-1)
else:
    print(len(path) - 1)
    print(*path)
