class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class adjacency_list():
    def __init__(self, n):
        self.head = [None]*n
    def add_edge(self, u, v, w):
        if self.head[u-1] == None :
            self.head[u-1] = Node((v, w))
        else:
            temp = self.head[u-1]
            while temp.next != None:
                temp = temp.next
            temp.next = Node((v, w))
    def print_list(self):
        for i in range(len(self.head)):
            temp = self.head[i]
            print(f"{i+1}:", end = " ")
            while temp != None:
                print(f"({temp.data[0]}, {temp.data[1]})", end = " ")
                temp = temp.next
            print()

n,m = map(int, input().split())
obj = adjacency_list(n)
X, Y, Z = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
for i in range(m):
    obj.add_edge(X[i], Y[i], Z[i])
    
obj.print_list()
