class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

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

class adjacency_list:
    def __init__(self, n):
        self.head = [None] * n
        self.nodes = [Node(i + 1) for i in range(n)]  
 
    def add_edge(self, u, v):
        node_v = Node(v)
        node_v.next = self.head[u - 1]
        self.head[u - 1] = node_v

        node_u = Node(u)
        node_u.next = self.head[v - 1]
        self.head[v - 1] = node_u 


def A_Football_Match(G, N):
    color = [0] * (N+1)
    max_cnt = 0

    for i in range(1, N+1):
        if color[i] == 0:
            Q = Queue()
            Q.enqueue(i)
            color[i] = 1
            cnt1 = 0
            cnt2 = 0

            while not Q.is_empty():
                node = Q.dequeue()
                if color[node] == 1:
                    cnt1 += 1
                else:
                    cnt2 += 1
                curr = G[node - 1]  
                while curr:
                    v = curr.data
                    if color[v] == 0:
                        if color[node] == 1:
                            color[v] = 2
                        else:
                            color[v] = 1
                        Q.enqueue(v)
                    elif color[v] == color[node]:
                        return -1  
                    curr = curr.next
            max_cnt += max(cnt1, cnt2)
    return max_cnt 

def solve():
    n, m = map(int, input().split())
    G = adjacency_list(n)
    for _ in range(m):
        u, v = map(int, input().split())
        G.add_edge(u, v)
    print(A_Football_Match(G.head, n))
solve()