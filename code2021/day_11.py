def solve_a():
    grid = []
    t = input()
    while len(t)>0:
        grid.append(list(map(int, t)))
        t = input()

    w = len(grid[0])
    h = len(grid)

    steps = 100

    flashes = [0]

    def flash():
        fg = False
        for x in range(w):
            for y in range(h):
                if grid[y][x] <= 9: continue
                fg = True
                flashed[y][x] = 1
                flashes[0] += 1
                grid[y][x] = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if 0<=x+dx<w and 0<=y+dy<h:
                            if flashed[y+dy][x+dx]: continue
                            grid[y+dy][x+dx] += 1
        if fg: flash()

    for step in range(steps):
        flashed = [[0]*w for _ in range(h)]
        for x in range(w):
            for y in range(h):
                grid[y][x] += 1
        flash()

    print(flashes[0])

def solve_b():
    grid = []
    t = input()
    while len(t)>0:
        grid.append(list(map(int, t)))
        t = input()

    w = len(grid[0])
    h = len(grid)

    steps = 100

    flashes = [0]

    def flash():
        fg = False
        for x in range(w):
            for y in range(h):
                if grid[y][x] <= 9: continue
                fg = True
                flashed[y][x] = 1
                flashes[0] += 1
                grid[y][x] = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if 0<=x+dx<w and 0<=y+dy<h:
                            if flashed[y+dy][x+dx]: continue
                            grid[y+dy][x+dx] += 1
        if fg: flash()

    step = 0
    while 1:
        flashed = [[0]*w for _ in range(h)]
        s = 0
        for x in range(w):
            for y in range(h):
                s += grid[y][x]
                grid[y][x] += 1
        if s == 0:
            print(step)
            break
        flash()
        step += 1

if __name__ == "__main__":
    solve_b()

