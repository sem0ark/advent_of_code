def solve_a():
    N = 50
    grid = [[[0]*N for i in range(N)] for j in range(N)]

    t = input()
    cx = cy = N//2 - 3
    y = 0
    while t:
        for x in range(len(t)):
            if t[x] == '#':
                grid[cx+x][cy+y][N//2] = 1
        y += 1
        t = input()

    def count(x, y, z):  # returns number of life cells !(don't count border)!
        res = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if dx==dy==dz==0: continue
                    res += grid[x+dx][y+dy][z+dz]
        return res

    cycles = 6
    for k in range(cycles):
        print(k)
        # compute changes
        to_change = []
        for x in range(1, N-1):
            for y in range(1, N-1):
                for z in range(1, N-1):
                    c = count(x, y, z)
                    if grid[x][y][z] == 1 and 2 <= c <= 3: continue
                    if grid[x][y][z] == 0 and c != 3: continue
                    to_change.append((x, y, z))

        # apply changes
        for (x, y, z) in to_change:
            grid[x][y][z] ^= 1

    res = 0
    for x in range(1, N-1):
        for y in range(1, N-1):
            for z in range(1, N-1):
                res += grid[x][y][z]
    print(res)

def solve_b():
    N = 30
    grid = [[[[0]*N for i in range(N)] for j in range(N)] for k in range(N)]

    t = input()
    cx = cy = N//2 - 3
    y = 0
    while t:
        for x in range(len(t)):
            if t[x] == '#':
                grid[cx+x][cy+y][N//2][N//2] = 1
        y += 1
        t = input()

    def count(x, y, z, w):  # returns number of life cells !(don't count border)!
        res = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    for dw in range(-1, 2):
                        if dx==dy==dz==dw==0: continue
                        res += grid[x+dx][y+dy][z+dz][w+dw]
        return res

    cycles = 6
    for k in range(cycles):
        print(k)
        # compute changes
        to_change = []
        for x in range(1, N-1):
            for y in range(1, N-1):
                for z in range(1, N-1):
                    for w in range(1, N-1):
                        c = count(x, y, z, w)
                        if grid[x][y][z][w] == 1 and 2 <= c <= 3: continue
                        if grid[x][y][z][w] == 0 and c != 3: continue
                        to_change.append((x, y, z, w))

        # apply changes
        for (x, y, z, w) in to_change:
            grid[x][y][z][w] ^= 1

    res = 0
    for x in range(N):
        for y in range(N):
            for z in range(N):
                for w in range(N):
                    res += grid[x][y][z][w]
    print(res)

if __name__ == "__main__":
    solve_b()

