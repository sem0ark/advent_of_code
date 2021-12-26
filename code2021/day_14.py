from collections import defaultdict

def solve():
    s = input()
    input()

    d = defaultdict(int)
    for i in range(1, len(s)): d[s[i-1]+s[i]] += 1
    counter = defaultdict(int)
    for i in s: counter[i] += 1
    s = d

    table = {}
    t = input()
    while len(t)>0:
        key, val = t.split(' -> ')
        table[key] = val
        t = input()

    steps = 40
    for _ in range(steps):
        nxt = defaultdict(int)
        for a in s.keys():
            t = table[a]
            counter[t] += s[a]
            nxt[a[0]+t] += s[a]
            nxt[t+a[1]] += s[a]
        s = nxt

    t = list(counter.values())
    t.sort()
    # print(t)
    print(t[-1] - t[0])


if __name__ == "__main__":
    solve()