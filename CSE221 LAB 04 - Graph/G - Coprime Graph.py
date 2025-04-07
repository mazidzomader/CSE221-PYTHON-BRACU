import math
class Coprime_Graph():
    def __init__(self, n):
        self.graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n) :
                if (i != j) :
                    if math.gcd(i+1, j+1) == 1:
                        self.graph[i].append(j+1)
        self.__result = []
    def queries_validity(self, u, v):
        temp = self.graph[u-1]
        if v <= len(temp):
            self.__result.append(temp[v-1])
        else :
            self.__result.append(-1)
    def get_result(self):
        return self.__result
n, m = map(int, input().split())
obj = Coprime_Graph(n)
for _ in range(m):
    u, v = map(int, input().split())
    obj.queries_validity(u, v)
for i in obj.get_result():
    print(i)
