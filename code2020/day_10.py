def solve_a():
    # get nums
    t = input()
    s = [0]
    while len(t)>0:
        s.append(int(t))
        t = input()

    s.sort()
    counter = [0,0,0]
    for i in range(1, len(s)):
        counter[s[i]-s[i-1]-1] += 1

    counter[-1] += 1

    print(counter[0]*counter[2])


def solve_b():
    t = input()
    s = [0]
    while len(t)>0:
        s.append(int(t))
        t = input()

    s.sort()
    s.append(s[-1]+3)
    paths = [0]*len(s)
    paths[0] = 1
    for i in range(len(paths)):
        c = 1
        while i+c<len(s) and s[i+c]-s[i] <= 3:
            paths[i+c] += paths[i]
            c += 1
    print(paths[-1])

if __name__ == "__main__":
    solve_b()