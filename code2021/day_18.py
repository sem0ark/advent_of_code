
class Tree:
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def __repr__(self):
        return f'[{self.l},{self.r}]'

def add_r(tr, n):
    print('add_r', tr, n)
    if type(tr.l)==type(0): tr.l += n
    else: add_r(tr.l, n)

def add_l(tr, n):
    print('add_l', tr, n)
    if type(tr.r)==type(0): tr.r += n
    else: add_l(tr.r, n)

def explode(tr, deep=1):
    if deep > 4 and type(tr.l) == type(0) and type(tr.r) == type(0):
        return (tr.l, tr.r, True)

    # process l
    if type(tr.l) != type(0):
        exp_l = explode(tr.l, deep+1)
        if exp_l is not None:
            (nl, nr, f_zero) = exp_l
            if f_zero: tr.l = 0
            p = tr
            k = tr.r
            while type(k) != type(0): p, k = k, k.l
            k.r += nl
            return (nl, None, False)

    # if type(tr.l) != type(0):
    #     res_1 = explode(tr.l, deep+1)
    #     print(tr, res_1)
    #     if res_1 is not None:
    #         (nl, nr, f_zero) = res_1
    #         if f_zero:
    #             tr.l = 0
    #             tr.r += nr
    #             return (nl, None, False)
    #         if nr is not None and type(tr.r) != type(0):
    #             print('add_r', tr.r, nr)
    #             add_r(tr.r, nr)
    #             nr = None
    #         return (nl, nr, False)

    # if type(tr.r) != type(0):
    #     res_2 = explode(tr.r, deep+1)
    #     print(tr, res_2)
    #     if res_2 is not None:
    #         (nl, nr, f_zero) = res_2
    #         if f_zero:
    #             tr.r = 0
    #             tr.l += nl
    #             return (None, nr, False)
    #         if nl is not None and type(tr.l) != type(0):
    #             print('add_l', tr.l, nl)
    #             add_l(tr.l, nl)
    #             nl = None
    #         return (nl, nr, False)
    # return None


def split(tr):
    if type(tr.l) == type(0) and tr.l > 9:
        tr.l = Tree(tr.l//2, tr.l - tr.l//2)
        return True
    if type(tr.r) == type(0) and tr.r > 9:
        tr.r = Tree(tr.r//2, tr.r - tr.r//2)
        return True
    if type(tr.r) != type(0): split(tr.r)
    if type(tr.l) != type(0): split(tr.l)


def add(a, b):
    s = Tree(a, b)
    r1 = explode(s)
    r2 = split(s)
    while r1 is not None or r2 is not None:
        r1 = explode(s)
        r2 = split(s)

    return s

def compute_mag(tr): # V
    nl = 0
    if type(tr.l) == type(0): nl = 3*tr.l
    else: nl = 3*compute_mag(tr.l)
    
    nr = 0
    if type(tr.r) == type(0): nr = 2*tr.r
    else: nr = 2*compute_mag(tr.r)

    return nl+nr

def solve_a():
    adders = []
    # t = input()
    t = '[1,[1,[1,[[2,2],1]]]]'
    while len(t)>0:
        t = t.replace('[', 'Tree(')
        t = t.replace(']', ')')
        adders.append(eval(t))
        t = input()

    s = adders[0]
    explode(s)
    # split(s)
    # for i in adders[1:]:
    #     print(s)
    #     s = add(s, i)
    print(s)
    print(compute_mag(s))


def solve_b():...

if __name__ == "__main__":
    solve_a()
