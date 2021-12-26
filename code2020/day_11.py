def solve_a():
    # get cells
    t = input()
    grid = []
    while len(t)>0:
        grid.append([0 if i=='L' else -1 for i in t])
        t = input()

    w = len(grid[0])
    h = len(grid)

    def simulate():
        to_change = []
        for y in range(h):
            for x in range(w):
                if grid[y][x] == -1: continue
                c = 0
                for x1 in range(max(x-1, 0), min(x+2, w)):
                    for y1 in range(max(y-1, 0), min(y+2, h)):
                        if x1 == x and y1 == y: continue
                        if grid[y1][x1] == -1: continue
                        c += grid[y1][x1]
                if grid[y][x] == 1 and c>=4: to_change.append((x, y))
                elif grid[y][x] == 0 and c==0: to_change.append((x, y))
        return to_change

    ch = []
    while 1:
        ch = simulate()
        if len(ch) == 0: break
        for (x, y) in ch: grid[y][x] ^= 1

    res = 0
    for x in range(w):
        for y in range(h):
            if grid[y][x] == 1:
                res += 1

    print(res)


def solve_b():
    # get cells
    t = input()
    grid = []
    while len(t)>0:
        grid.append([0 if i=='L' else -1 for i in t])
        t = input()

    w = len(grid[0])
    h = len(grid)

    def get_neibs(x, y):
        d = [
            (-1, 0),(1, 0),(0, 1),(0, -1),
            (-1, 1),(1, 1),(-1, -1),(1, -1),
        ]
        neibs = []
        for dx, dy in d:
            cx, cy = x+dx, y+dy
            while 0<=cx+dx<w and 0<=cy+dy<h and grid[cy][cx] < 0:
                cx, cy = cx+dx, cy+dy
            if 0<=cx<w and 0<=cy<h and grid[cy][cx] > -1:
                neibs.append((cx, cy))
        # print(x, y, neibs)
        return neibs



    cell_view = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 0:
                cell_view.append([(x, y)])
                cell_view[-1] += get_neibs(x, y)

    def simulate():
        to_change = []
        for cell in cell_view:
            x, y = cell[0]
            c = 0
            if len(cell) > 1: c = sum(grid[cy][cx] for cx, cy in cell[1:])
            if grid[y][x] == 1 and c>=5: to_change.append((x, y))
            elif grid[y][x] == 0 and c==0: to_change.append((x, y))
        return to_change

    ch = []
    while 1:
        ch = simulate()
        if len(ch) == 0: break
        for (x, y) in ch: grid[y][x] ^= 1
        # print()
        # for i in grid: print(''.join('L#.'[j] for j in i))



    res = 0
    for x in range(w):
        for y in range(h):
            if grid[y][x] == 1:
                res += 1

    print(res)

if __name__ == "__main__":
    solve_b()


# .......L.
# ...L.....
# .L.......
# .........
# ..LL....L
# ....L....
# .........
# L........
# ...L.....