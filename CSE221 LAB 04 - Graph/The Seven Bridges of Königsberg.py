class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class adjecency_list():
    def __init__(self, n):
        self.head = [[] for _ in range(n)]
        self.degree = [0]*n
    def add_edge(self, u, v):
        self.head[u - 1].append(v)
        self.head[v - 1].append(u)
        self.degree[u - 1] += 1
        self.degree[v - 1] += 1

n, m = map(int, input().split())
one_end = list(map(int, input().split()))
other_end = list(map(int, input().split()))
obj = adjecency_list(n)
for i in range(m):
    obj.add_edge(one_end[i], other_end[i])
# obj.print_list()
degree = obj.degree

def seven_kings_of_Konigsberg(arr):
    even_flag = True
    for i in arr:
        if i % 2 == 1 :
            even_flag = False
            break
    exact_two_odd = 0
    for i in arr:
        if i % 2 == 1 :
            exact_two_odd += 1
    if (even_flag) or (exact_two_odd == 2):
        print("YES")
    else:
        print("NO")
seven_kings_of_Konigsberg(degree)
