class Queue:
    def __init__(self):
        self.items = []
        self.head = 0  

    def is_empty(self):
        return self.head == len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.items[self.head]
        self.head += 1
        
        if self.head > 10000:
            self.items = self.items[self.head:]
            self.head = 0
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[self.head]

    def size(self):
        return len(self.items) - self.head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.colour = 0
        self.distance = -1
        self.predecessor = None

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

def bfs(G, start_node):
    for node in G.nodes:
        node.colour = 0
        node.distance = -1
        node.predecessor = None

    Q = Queue()
    start_node.colour = 1
    start_node.distance = 0
    Q.enqueue(start_node)

    farthest_node = start_node
    max_distance = 0

    while not Q.is_empty():
        u = Q.dequeue()

        if u.distance > max_distance:
            max_distance = u.distance
            farthest_node = u

        temp = G.head[u.data - 1]
        while temp:
            v = G.nodes[temp.data - 1]
            if v.colour == 0:
                v.colour = 1
                v.distance = u.distance + 1
                v.predecessor = u
                Q.enqueue(v)
            temp = temp.next

    return farthest_node, max_distance

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.data)
        node = node.predecessor
    return path[::-1]

def find_diameter(G, start_node):
    farthest_node_from_start, _ = bfs(G, start_node)
    farthest_node_from_first_bfs, diameter = bfs(G, farthest_node_from_start)
    path = reconstruct_path(farthest_node_from_first_bfs)
    print(diameter)
    print(path[0], path[-1])

N = int(input())
G = adjacency_list(N)

for _ in range(N - 1):
    u, v = map(int, input().split())
    G.add_edge(u, v)

start_node = G.nodes[0]
find_diameter(G, start_node)
