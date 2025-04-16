# Without stack
import sys
sys.setrecursionlimit(20 * 100000 + 5)
 
def DFS_visit(grid, row, col, status):
    status[row][col] = True
    count = 0
    if grid[row][col] == "D":
        count += 1
 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
    for m, n in directions:
        new_row, new_col = row + m, col + n
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and not status[new_row][new_col] and grid[new_row][new_col] != '#':
            count += DFS_visit(grid, new_row, new_col, status)
    
    return count
 
n, m = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(n)]
 
status = [[False for _ in range(m)] for _ in range(n)]
diamond = 0
 
for i in range(n):
    if "D" not in grid[i]:
        continue
    
    for j in range(m):
        if not status[i][j] and grid[i][j] != "#":
            count = DFS_visit(grid, i, j, status)
            diamond = max(diamond, count)
 
print(diamond)
