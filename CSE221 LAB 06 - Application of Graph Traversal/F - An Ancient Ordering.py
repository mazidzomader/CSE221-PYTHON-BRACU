import sys
sys.setrecursionlimit(2*10000)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.visited = False
        self.color = "White"

class adjacency_list:
    def __init__(self, n):
        self.head = [None] * n
        self.nodes = [Node(i + 1) for i in range(n)]

    def add_edge(self, u, v):
        new_node_v = Node(v)
        new_node_v.next = self.head[u - 1]
        self.head[u - 1] = new_node_v

def TopoSort(G, used_chars):
    L = None
    for i in range(26, 0, -1):
        if used_chars[i - 1]:
            u = G.nodes[i - 1]
            if not u.visited:
                L = DFS(G, u, L)
    return L

def DFS(G, u, L):
    u.visited = True
    temp = G.head[u.data - 1]
    while temp:
        v = G.nodes[temp.data - 1]
        if not v.visited:
            L = DFS(G, v, L)
        temp = temp.next
    L = Node(u.data, L)
    return L

def cycle_detector(G, used_chars):
    for i in range(1, 27):
        if used_chars[i - 1]:
            u = G.nodes[i - 1]
            if u.color == "White":
                if DFS_cycle(G, u):
                    return True
    return False

def DFS_cycle(G, u):
    u.color = "Gray"
    temp = G.head[u.data - 1]
    while temp:
        v = G.nodes[temp.data - 1]
        if v.color == "White":
            if DFS_cycle(G, v):
                return True
        elif v.color == "Gray":
            return True
        temp = temp.next
    u.color = "Black"
    return False

def solve():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input().strip())
    
    G = adjacency_list(26)
    
    used_chars = [False] * 26
    for i in words:
        for c in i:
            used_chars[ord(c) - ord('a')] = True
    
    flag = False
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        if len(w1) > len(w2) and w1.startswith(w2):
            flag = True
            break
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                u = ord(w1[j]) - ord('a') + 1
                v = ord(w2[j]) - ord('a') + 1
                G.add_edge(u, v)
                break

    if flag:
        print(-1)
        return

    if cycle_detector(G, used_chars):
        print(-1)
        return

    L = TopoSort(G, used_chars)
    
    result = []
    while L:
        char_idx = L.data - 1
        result.append(chr(ord('a') + char_idx))
        L = L.next
    
    print(''.join(result))

solve()