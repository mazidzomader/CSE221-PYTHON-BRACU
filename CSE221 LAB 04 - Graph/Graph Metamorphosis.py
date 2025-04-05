class graph_metamorphosis():
    def __init__(self, n):
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
    def print_matrix(self):
        for i in (self.matrix):
            print(" ".join(map(str, i)))
n = int(input())
obj = graph_metamorphosis(n)
for i in range(n):
    x = list(map(int, input().split()))
    for ii in range(1,x[0]+1):
        obj.add_edge(i, x[ii])
obj.print_matrix()
