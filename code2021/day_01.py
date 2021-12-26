def solve_a():
    s = []
    t = input()
    while len(t)>0:
        s.append(int(t))
        t = input()

    c = 0

    for i in range(1, len(s)):
        if s[i-1] < s[i]:
            c += 1

    print(c)

def solve_b():
    s = []
    t = input()
    while len(t)>0:
        s.append(int(t))
        t = input()

    c = 0

    for i in range(3, len(s)):
        if s[i-3] < s[i]:
            c += 1

    print(c)

if __name__ == "__main__":
    solve_b()
