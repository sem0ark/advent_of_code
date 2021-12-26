
def solve_a():
    q = []
    t = input()
    while len(t)>0:
        n = ['off', 'on'].index(t.split(' ')[0])
        x, y, z = t.split(' ')[1].split(',')
        x = tuple(map(int, x.replace('x=', '').split('..')))
        y = tuple(map(int, y.replace('y=', '').split('..')))
        z = tuple(map(int, z.replace('z=', '').split('..')))
        q.append((n, x, y, z))
        t = input()

    arr = [[[0]*202 for i in range(202)] for j in range(202)]

    for i in q:
        n, (x1, x2), (y1, y2), (z1, z2) = i
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    arr[x+100][y+100][z+100] = n

    print(sum(sum(sum(j) for j in i) for i in arr))

def solve_b():...

if __name__ == "__main__":
    solve_a()
