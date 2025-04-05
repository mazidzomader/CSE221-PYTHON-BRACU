class adjacency_matrix():
    def __init__(self, n):
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

    def add_edge(self, u, v, w):
        self.matrix[u-1][v-1] = w
    def print_matrix(self):
        for i in (self.matrix):
            print(" ".join(map(str, i)))
n, m = map(int, input().split())
obj = adjacency_matrix(n)
for _ in range(m):
    U, V, W = map(int, input().split())
    obj.add_edge(U, V, W)
obj.print_matrix()
