def solve_a():
    t = input()
    grid = []
    while len(t)>0:
        grid.append([int(i) for i in t])
        t = input()

    res = 0
    w = len(grid[0])
    h = len(grid)
    for x in range(w):
        for y in range(h):
            fg = True
            if 0<=x+1<w and 0<=y<h: fg = fg and grid[y][x+1] > grid[y][x]
            if 0<=x<w and 0<=y+1<h: fg = fg and grid[y+1][x] > grid[y][x]
            if 0<=x<w and 0<=y-1<h: fg = fg and grid[y-1][x] > grid[y][x]
            if 0<=x-1<w and 0<=y<h: fg = fg and grid[y][x-1] > grid[y][x]
            if fg:
                res += grid[y][x]+1
    print(res)

def solve_b():
    t = input()
    grid = []
    while len(t)>0:
        grid.append([int(i) for i in t])
        t = input()

    w = len(grid[0])
    h = len(grid)
    
    used = [[0]*w for _ in range(h)]
    basin_sizes = []

    dr = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    def get_size(x, y):
        c = [0]
        def dfs(x, y):
            # print(x, y, c)
            used[y][x] = 1
            c[0] += 1
            for dx, dy in dr:
                nx = x+dx
                ny = y+dy
                if 0<=nx<w and 0<=ny<h and used[ny][nx]==0 and 9>grid[ny][nx]>=grid[y][x]:
                    dfs(nx, ny)
        dfs(x, y)
        return c[0]
    
    for x in range(w):
        for y in range(h):
            fg = True
            if 0<=x+1<w and 0<=y<h: fg = fg and grid[y][x+1] > grid[y][x]
            if 0<=x<w and 0<=y+1<h: fg = fg and grid[y+1][x] > grid[y][x]
            if 0<=x<w and 0<=y-1<h: fg = fg and grid[y-1][x] > grid[y][x]
            if 0<=x-1<w and 0<=y<h: fg = fg and grid[y][x-1] > grid[y][x]
            if fg:
                basin_sizes.append(get_size(x, y))
                print(x, y, basin_sizes[-1])
    basin_sizes.sort()
    print(basin_sizes)


if __name__ == "__main__":
    solve_b()