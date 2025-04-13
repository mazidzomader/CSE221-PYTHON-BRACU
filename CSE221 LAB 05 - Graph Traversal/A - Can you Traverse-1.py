class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return len(self.items) == 0
 
    def enqueue(self, item):
        self.items.append(item)
 
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)
 
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]
 
    def size(self):
        return len(self.items)
 
    def display(self):
        print("Queue:", self.items)
 
 
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
 
    def print_list(self):
        for i in range(len(self.head)):
            temp = self.head[i]
            print(f"{i + 1}:", end=" ")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()
 
 
def bfs(G, start_node):
    for node in G.nodes:
        node.colour = 0  
 
    Q = Queue()
    start_node.colour = 1  
    Q.enqueue(start_node)
 
    while not Q.is_empty():
        u = Q.dequeue()
        print(u.data, end=" ")
 
        temp = G.head[u.data - 1]  
        while temp:
            v = G.nodes[temp.data - 1]  
            if v.colour == 0:  
                v.colour = 1
                Q.enqueue(v)
            temp = temp.next
 
 
# ----------- INPUT ------------
n, m = map(int, input().split())
obj = adjacency_list(n)
 
for _ in range(m):
    X, Y = map(int, input().split())
    obj.add_edge(X, Y)
 
 
bfs(obj, obj.nodes[0])  
