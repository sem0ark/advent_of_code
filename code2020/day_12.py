def solve_a():
    t = input()
    x, y = 0, 0
    d = 0
    dirs = [
        (1, 0), (0, 1), (-1, 0), (0, -1)
    ]
    while len(t)>0:
        h = t[0]
        c = int(t[1:])
        if h in 'ESWN':
            ind = 'ESWN'.index(h)
            x += dirs[ind][0]*c
            y += dirs[ind][1]*c
        elif h == 'R': d = (d+(c//90)) % 4
        elif h == 'L': d = (4+d-(c//90)) % 4
        elif h == 'F':
            x += dirs[d][0]*c
            y += dirs[d][1]*c
        t = input()

    print(abs(x) + abs(y))

def solve_b():
    t = input()
    ship_x, ship_y = 0, 0
    aim_x, aim_y = 10, 1
    dirs = [
        (1, 0), (0, -1), (-1, 0), (0, 1)
    ]
    while len(t)>0:
        h = t[0]
        c = int(t[1:])
        if h in 'ESWN':
            ind = 'ESWN'.index(h)
            aim_x += dirs[ind][0]*c
            aim_y += dirs[ind][1]*c
        elif h == 'R':
            for _ in range(c//90):
                aim_x, aim_y = aim_y, -aim_x
        elif h == 'L':
            for _ in range(c//90):
                aim_x, aim_y = -aim_y, aim_x
        elif h == 'F':
            ship_x += c*aim_x
            ship_y += c*aim_y
        print(aim_x, aim_y, ship_x, ship_y)
        t = input()

    print(abs(ship_x) + abs(ship_y))

if __name__ == "__main__":
    solve_b()