def DFS_visit(grid, row, col, status):
    stack = [(row, col)]
    count = 0
    while stack:
        r, c = stack.pop()
        if status[r][c]:
            continue
        status[r][c] = True
        if grid[r][c] == "D":
            count += 1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for m, n in directions:
            new_row, new_col = r + m, c + n
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) :
                if (status[new_row][new_col] == False) and grid[new_row][new_col] != '#':
                    stack.append((new_row, new_col))
    return count

n, m = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(n)]

status = [[False for _ in range(m)] for _ in range(n)]
diamond = 0

for i in range(n):
    if "D" not in grid[i]:
        continue
    
    for j in range(m):
        if (status[i][j] == False) and grid[i][j] != "#":
            count = DFS_visit(grid, i, j, status)
            diamond = max(diamond, count)

print(diamond)
