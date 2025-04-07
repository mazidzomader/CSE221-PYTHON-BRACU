class Node():
    def __init__(self, n):
        self.data = n
        self.in_degree = 0
        self.out_degree = 0
        self.next = None

class Edge_Queries():
    def __init__(self, n):
        self.heads = [Node(i + 1) for i in range(n)] 
    
    def add_edge(self, u, v):
        self.heads[u - 1].out_degree += 1  
        self.heads[v - 1].in_degree += 1  
    
    def get_heads(self):
        return self.heads

n, m = map(int, input().split())
one_end = list(map(int, input().split()))
other_end = list(map(int, input().split()))

obj = Edge_Queries(n)
for i in range(m):
    obj.add_edge(one_end[i], other_end[i])

for node in obj.get_heads():
    print(node.in_degree - node.out_degree, end=" ")
