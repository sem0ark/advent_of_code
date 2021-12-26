def solve_ab():
    t = input()
    s = []
    mxx = 0
    mxy = 0
    while len(t)>0:
        (a, b), (c, d) = [map(int, i.split(',')) for i in t.split(' -> ')]
        mxx = max(mxx, a, c)
        mxy = max(mxy, b, d)
        s.append((a, b, c, d))
        t = input()
    
    grid = [[0]*(mxy+1) for _ in range(mxx+1)]

    def sign(a):
        if a == 0: return 0
        if a < 0: return -1
        if a > 0: return 1

    for i in range(len(s)):
        x1, y1, x2, y2 = s[i]
        d = (sign(x2-x1), sign(y2-y1))
        for k in range(1, max(abs(x1-x2), abs(y1-y2)), 1): grid[x1 + d[0]*k][y1 + d[1]*k] += 1
        grid[x1][y1] += 1
        grid[x2][y2] += 1

    # for i in grid:
    #     print(''.join(map(str, i)))

    c = 0
    for x in range(mxx+1):
        for y in range(mxy+1):
            if grid[x][y] > 1:
                c += 1

    print(c)


if __name__ == "__main__":
    solve_ab()
