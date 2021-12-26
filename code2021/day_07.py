def solve_a():
    s = [int(i) for i in input().split(',')]
    s.sort()
    mid = s[len(s)//2]
    res = 0
    for pos in s:
        res += abs(pos-mid)

    print(res)

def solve_b():
    s = [int(i) for i in input().split(',')]
    
    def calc_fuel(m):
        res = 0
        for i in s:
            f = abs(i-m)
            res += f*(f+1)//2
        return res

    min_res = 100000000000
    for m in range(min(s), max(s)+1):
        min_res = min(min_res, calc_fuel(m))
    print(min_res)

if __name__ == "__main__":
    solve_b()
