def solve_a():
    # get nums
    t = input()
    s = [[0, 0] for _ in range(len(t))]
    while len(t)>0:
        for i in range(len(t)): s[i][int(t[i])] += 1
        t = input()

    # get gamma, epsilon
    gamma = ''
    epsilon = ''
    for i in s:
        if i[0]>i[1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    print(int(gamma, 2)*int(epsilon, 2))

def solve_b():
    # get nums
    t = input()
    s = []
    while len(t)>0:
        s.append(t)
        t = input()

    def get_popular(ind, s):
        n = len(s)
        c = 0
        for num in s: c += int(num[ind])
        if c >= n-c: return [t for t in s if t[ind]=='1']
        return [t for t in s if t[ind]=='0']

    def get_unpopular(ind, s):
        n = len(s)
        c = 0
        for num in s: c += int(num[ind])
        if c >= n-c: return [t for t in s if t[ind]=='0']
        return [t for t in s if t[ind]=='1']

    t = s.copy()
    i = 0
    while len(t) > 1:
        t = get_popular(i, t)
        i += 1
    oxygen_lvl = int(t[0], 2)

    t = s.copy()

    i = 0
    while len(t) > 1:
        t = get_unpopular(i, t)
        i += 1
    co2_lvl = int(t[0], 2)
    
    print(oxygen_lvl * co2_lvl)

if __name__ == "__main__":
    solve_b()