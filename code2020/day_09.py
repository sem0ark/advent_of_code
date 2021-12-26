from collections import defaultdict
from queue import Queue

def solve_a():
    s = defaultdict(int)
    q = Queue()

    t = input()
    for _ in range(25+1):
        c = int(t)
        s[c] += 1
        q.put(c)
        t = input()

    while t:
        pr = q.get()
        s[pr] -= 1
        if s[pr] == 0: del s[pr]

        c = int(t)
        good = False
        for i in s.keys():
            if (c == 2*i and s[i]>1) or (c-i in s):
                good = True
                break

        if not good:
            print(c)

        q.put(c)
        s[c] += 1
        t = input()

def solve_b():
    all_nums = []
    s = defaultdict(int)
    q = Queue()

    t = input()
    for _ in range(25+1):
        c = int(t)
        all_nums.append(c)
        s[c] += 1
        q.put(c)
        t = input()

    bad_num = None

    while t:
        pr = q.get()
        s[pr] -= 1
        if s[pr] == 0: del s[pr]

        c = int(t)
        all_nums.append(c)
        good = False
        for i in s.keys():
            if (c == 2*i and s[i]>1) or (c-i in s):
                good = True
                break

        if not good:
            bad_num = c
            print(c)

        q.put(c)
        s[c] += 1
        t = input()

    a = 0
    b = 1
    while b < len(all_nums) and sum(all_nums[a:b+1]) != bad_num:
        _sum = sum(all_nums[a:b+1])
        if _sum > bad_num: a += 1
        if _sum < bad_num: b += 1

    print(a, b, max(all_nums[a:b+1])+min(all_nums[a:b+1]))

if __name__ == "__main__":
    solve_b()
