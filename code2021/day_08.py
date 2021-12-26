def solve_a():
    t = input()
    c = 0
    while len(t)>0:
        nums, inputs = t.split(' | ')
        inputs = inputs.split()
        for i in inputs:
            if len(i) in [2, 3, 4, 7]: c += 1
        t = input()
    print(c)

def solve_b():
    from collections import defaultdict
    t = input()
    c = 0

    def its(a, b):
        return len(b.symmetric_difference(a))

    res = 0

    while len(t)>0:
        nums, inputs = t.split(' | ')
        nums = nums.split()
        inputs = inputs.split()
        d = defaultdict(list)
        for i in nums: d[len(i)].append(set(i))
        dig = [None]*10
        dig[1] = d[2][0]
        dig[7] = d[3][0]
        dig[8] = d[7][0]
        dig[4] = d[4][0]
        
        for num in d[6]:
            if its(num, dig[7])==3 and its(num, dig[4])==2: dig[9] = num
            elif its(num, dig[7])==3 and its(num, dig[4])==4: dig[0] = num
            elif its(num, dig[7])==5 and its(num, dig[4])==4: dig[6] = num

        for num in d[5]:
            if len(num - dig[9])==0 and its(dig[7], num)==2: dig[3] = num
            elif len(num - dig[9])==0 and its(dig[7], num)==4: dig[5] = num
            else: dig[2] = num

        if None in dig:
            print(nums, dig)


        cur_res = ''
        for i in inputs:
            for j in range(10):
                if dig[j] == set(i):
                    cur_res += str(j)


        cur_res = int(cur_res)
        res += cur_res

        t = input()

    print(res)

if __name__ == "__main__":
    solve_b()


