from collections import defaultdict

def solve_a():
    grid = []
    t = input()
    while len(t)>0:
        grid.append(list(map(int, t)))
        t = input()

    w = len(grid[0])
    h = len(grid)
    dp = [[0]*w for i in range(h)]

    for i in range(1, w): dp[0][i] = dp[0][i-1]+grid[0][i]
    for i in range(1, h): dp[i][0] = dp[i-1][0]+grid[i][0]

    for i in range(1, h):
        for j in range(1, w):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
    
    # for i in dp: print(i)
    
    print(dp[-1][-1])

def solve_b():
    from heapq import heappush, heappop
    from math import inf

    grid = []
    t = input()
    while len(t)>0:
        grid.append(list(map(int, t)))
        t = input()
    
    w = len(grid[0])
    h = len(grid)
    
    for _ in range(4):
        for i in range(h):
            for j in range(w):
                if grid[i][-w]==9: grid[i] += [1]
                else: grid[i] += [grid[i][-w]+1]
    for _ in range(4):
        for i in range(h):
            grid.append([1 if j==9 else j+1 for j in grid[-h]])

    
    w = len(grid[0])
    h = len(grid)
    
    dist = [[inf]*w for i in range(h)]
    d = [
        (1,0),
        (0,1),
        (-1,0),
        (0,-1),
    ]
    dist[0][0] = 0

    q = [(0, (0,0))]
    proc = set()
    while q:
        x, y = heappop(q)[1]
        if (x, y) in proc: continue
        proc.add((x, y))
        for (dx, dy) in d:
            nx, ny = x+dx, y+dy
            if 0<=nx<w and 0<=ny<h:
                if dist[y][x]+grid[ny][nx] < dist[ny][nx]:
                    dist[ny][nx] = dist[y][x]+grid[ny][nx]
                    heappush(q, (dist[ny][nx], (nx, ny)))

    print(dist[-1][-1])

if __name__ == "__main__":
    solve_b()
