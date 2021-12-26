def solve_a():
    points = [3, 57, 1197, 25137]
    alf_a = '([{<'
    alf_b = ')]}>'


    res = 0
    t = input()
    while len(t)>0:
        stack = []
        for k, ch in enumerate(t):
            if ch in alf_a:
                br_index = alf_a.index(ch)
                stack.append(br_index)
            elif ch in alf_b:
                br_index = alf_b.index(ch)
                if not stack or stack[-1] != br_index:
                    res += points[br_index]
                    # print(stack, k, alf_b[br_index])
                    break
                else:
                    stack.pop()
        t = input()
    print(res)

def solve_b():
    points = [1, 2, 3, 4]
    alf_a = '([{<'
    alf_b = ')]}>'


    res = []
    t = input()
    while len(t)>0:
        stack = []
        for ch in t:
            fg = True
            if ch in alf_a:
                br_index = alf_a.index(ch)
                stack.append(br_index)
            elif ch in alf_b:
                br_index = alf_b.index(ch)
                # discard bad
                if not stack or stack[-1] != br_index:
                    fg = False
                    break
                else: stack.pop()
        # calculate scores
        if fg:
            cur = 0
            while stack:
                cur *= 5
                cur += points[stack.pop()]
            res.append(cur)
        t = input()
    res.sort()
    # print(res)
    print(res[len(res)//2])

if __name__ == "__main__":
    solve_b()