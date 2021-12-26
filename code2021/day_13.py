def solve_a():
    dots = set()
    t = input()
    while len(t)>0:
        x, y = map(int, t.split(','))
        dots.add((x, y))
        t = input()

    # input()

    t = input()
    while len(t)>0:
        a, n = t.split(' ')[-1].split('=')
        n = int(n)
        nxt_dots = set()
        if a == 'x':
            for (x, y) in dots:
                if x > n: nxt_dots.add((x - 2*abs(x-n), y))
                else: nxt_dots.add((x, y))
        if a == 'y':
            for (x, y) in dots:
                if y > n: nxt_dots.add((x, y - 2*abs(y-n)))
                else: nxt_dots.add((x, y))
        dots = nxt_dots
        t = input()
        break

    print(len(dots))

def solve_b():
    dots = set()
    t = input()
    while len(t)>0:
        x, y = map(int, t.split(','))
        dots.add((x, y))
        t = input()

    # input()

    t = input()
    while len(t)>0:
        a, n = t.split(' ')[-1].split('=')
        n = int(n)
        nxt_dots = set()
        if a == 'x':
            for (x, y) in dots:
                if x > n: nxt_dots.add((x - 2*abs(x-n), y))
                else: nxt_dots.add((x, y))
        if a == 'y':
            for (x, y) in dots:
                if y > n: nxt_dots.add((x, y - 2*abs(y-n)))
                else: nxt_dots.add((x, y))
        dots = nxt_dots
        t = input()

    maxx = max(i[0] for i in dots)
    minx = min(i[0] for i in dots)
    maxy = max(i[1] for i in dots)
    miny = min(i[1] for i in dots)

    w = maxx - minx + 1
    h = maxy - miny + 1

    grid = [['.']*w for _ in range(h)]
    for (x, y) in dots: grid[y-miny][x-minx] = '#'

    for i in grid: print(''.join(i))

    print(len(dots))

if __name__ == "__main__":
    solve_b()
