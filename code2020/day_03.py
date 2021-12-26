def solve_a():
    s = []
    t = input()
    while len(t)>0:
        s.append(t)
        t = input()

    width = len(s[0])
    height = len(s)

    cur_x = 0
    cur_y = 0
    dx = 3
    dy = 1

    tree_count = 0

    while cur_y < height:
        if s[cur_y][cur_x] == '#': tree_count += 1
        cur_x = (cur_x+dx) % width
        cur_y += dy

    print(tree_count)

def solve_b():
    s = []
    t = input()
    while len(t)>0:
        s.append(t)
        t = input()

    width = len(s[0])
    height = len(s)

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

    d = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    res = 1

    for (dx,dy) in d:
        cur_x = 0
        cur_y = 0

        tree_count = 0

        while cur_y < height:
            if s[cur_y][cur_x] == '#': tree_count += 1
            cur_x = (cur_x+dx) % width
            cur_y += dy

        res *= tree_count

    print(res)

if __name__ == "__main__":
    solve_b()