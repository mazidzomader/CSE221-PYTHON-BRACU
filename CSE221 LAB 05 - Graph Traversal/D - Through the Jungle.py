class Node:
    def __init__(self, data):
        self.data = data
        self.colour = 0
        self.parent = None

class adjacency_list:
    def __init__(self, n):
        self.head = [[] for _ in range(n)]
        self.nodes = [Node(i + 1) for i in range(n)]

    def add_edge(self, u, v):
        self.head[u - 1].append(v)

    def sort_adj(self):
        for v in self.head:
            v.sort()

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
        return self.outbox.pop()

def bfs(G, start_node):
    for node in G.nodes:
        node.colour = 0
        node.parent = None

    Q = Queue()
    start_node.colour = 1
    Q.enqueue(start_node)

    while not Q.is_empty():
        u = Q.dequeue()
        for V in G.head[u.data - 1]:
            v = G.nodes[V - 1]
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

n, m, s, d, k = map(int, input().split())
obj = adjacency_list(n)


for i in range(m):
    X, Y = map(int, input().split())
    obj.add_edge(X, Y)

obj.sort_adj()
def through_the_jungle(G, s, d, k):
    if s == d == k:
        print(0)
        print(s)
        return

    bfs(G, G.nodes[s - 1])  
    if k != s and G.nodes[k - 1].parent is None:
        print(-1)
        return
    path1 = path_finder(G.nodes[k - 1])  

    bfs(G, G.nodes[k - 1])
    if d != k and G.nodes[d - 1].parent is None:
        print(-1)
        return
    path2 = path_finder(G.nodes[d - 1])  

    path3 = path1 + path2[1:]
    print(len(path3) - 1)
    print(*path3)

through_the_jungle(obj, s,d, k)


