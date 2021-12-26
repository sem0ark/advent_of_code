def solve_a():
    s = []
    t = input()
    while len(t)>0:
        s.append(t)
        t = input()

    max_id = 0

    for p in s:
        p = p.replace('B', '1')
        p = p.replace('F', '0')
        p = p.replace('R', '1')
        p = p.replace('L', '0')
        row = int(p[0:7], 2)
        col = int(p[7:], 2)
        cur_id = row*8+col
        max_id = max(cur_id, max_id)

    print(max_id)

def solve_b():
    s = []
    t = input()
    while len(t)>0:
        s.append(t)
        t = input()

    max_id = 0

    for i in range(len(s)):
        p = s[i]
        p = p.replace('B', '1')
        p = p.replace('F', '0')
        p = p.replace('R', '1')
        p = p.replace('L', '0')
        row = int(p[0:7], 2)
        col = int(p[7:], 2)
        cur_id = row*8+col
        s[i] = cur_id

    s.sort()

    for i in range(1, len(s)):
        if s[i]-s[i-1] > 1:
            print(s[i-1]+1)

if __name__ == "__main__":
    solve_b()
