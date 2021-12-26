def solvea():
    s = []
    t = input()
    while len(t) > 0:
        s.append(int(t))
        t = input()
    # print(s)
    n = len(s)
    for i in range(n):
        a = s[i]
        if (2020-a) in s:
            print(a*(2020-a))
            return

def solveb():
    s = []
    t = input()
    while len(t) > 0:
        s.append(int(t))
        t = input()
    # print(s)
    n = len(s)
    for i in range(n-1):
        for j in range(i+1, n):
            a, b = s[i], s[j]
            if (2020-a-b) in s:
                print(a*b*(2020-a-b))
                return

if __name__ == "__main__":
    solve()