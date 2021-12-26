from math import sqrt, floor, ceil

def sign(a):
    if a>0: return 1
    if a<0: return -1
    return 0


def get_x_pos(vx, n):
    if n <= abs(vx): return sign(vx) * abs(n*abs(vx)-n*(n-1)//2)
    return sign(vx) * abs(vx*vx-(vx*vx-abs(vx))//2)

def get_y_pos(vy, n):
    return n*vy-n*(n-1)//2

def solve_quad(a, b, c):
    d = b*b - 4*a*c
    if d < 0: return None
    d = sqrt(d)
    n1 = (-b-d)/2/a
    n2 = (-b+d)/2/a
    return (n1, n2)


def get_n(vx, vy, target_coords):
    x1, x2, y1, y2 = target_coords

    if y1>=0 and y2>=0:
        res_1 = solve_quad(1, -(2*vy+1), 2*y1)
        res_2 = solve_quad(1, -(2*vy+1), 2*y2)
    else:
        res_1 = solve_quad(1, -(2*vy+1), 2*y2)
        res_2 = solve_quad(1, -(2*vy+1), 2*y1)

    # if res_1 is None and res_2 is None: return None
    
    def in_borders(x, y):
        return x1<=x<=x2 and y1<=y<=y2

    
    n1_1 = floor(max(min(res_1), 0))
    n2_1 = ceil(max(res_1))
    if res_2 is None:
        st = floor(max(min(n1_1, n2_1),0))
        en = ceil(max(n1_1, n2_1, n1_2, n2_2,0))
    else:
        n1_2 = ceil(max(min(res_2), 0))
        n2_2 = floor(max(res_2))
        st = floor(max(max(n1_1, n2_1, n1_2, n2_2),0))
        en = ceil(max(n1_1, n2_1, n1_2, n2_2,0))

    

    # print(st, en)
    res = None

    for i in range(max(st-1, 0), en+1):
        x = get_x_pos(vx, i)
        y = get_y_pos(vy, i)
        # print(x, y)
        if in_borders(x, y): res = i
    
    return res

def solve_a_b():

    t = input().replace('y=','').replace('x=','').replace(',','').split()[2:]
    x1, x2 = map(int, t[0].split('..'))
    y1, y2 = map(int, t[1].split('..'))
    del t
    # x1, x2, y1, y2 = 20,30,-10,-5
    
    target_coords = (x1, x2, y1, y2)
    max_y = -10000
    c = 0
    # vx, vy = 6, 9
    
    for vx in range(600):
        for vy in range(-1000, 1000):
            n = get_n(vx, vy, target_coords)
            if n is None: continue
            c += 1
            if vy > 0 and n >= vy: max_y = max(max_y, get_y_pos(vy, vy))
            max_y = max(max_y, 0, get_y_pos(vy, n))
            print(c)
    print(max_y)
    print(c)
    

if __name__ == "__main__":
    solve_a_b()

