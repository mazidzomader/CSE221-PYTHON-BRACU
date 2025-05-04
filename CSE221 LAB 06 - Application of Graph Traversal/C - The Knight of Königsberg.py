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

def min_knight_moves(N, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0

    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    flag = [[0] * N for _ in range(N)]
    queue = Queue()
    queue.enqueue((x1 - 1, y1 - 1, 0))
    flag[x1 - 1][y1 - 1] = 1

    while not queue.is_empty():
        x, y, steps = queue.dequeue()

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N and flag[nx][ny] == 0:
                if nx == x2 - 1 and ny == y2 - 1:
                    return steps + 1
                flag[nx][ny] = 1
                queue.enqueue((nx, ny, steps + 1))

    return -1

N = int(input())
x1, y1, x2, y2 = map(int, input().split())
print(min_knight_moves(N, x1, y1, x2, y2))
