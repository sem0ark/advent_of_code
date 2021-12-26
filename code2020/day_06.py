def solve_a():

    with open('in.txt', 'r') as f:
        text = f.read()
        s = text.split('\n\n')

    c = 0
    
    for i in s:
        i = i.replace('\n', '')
        i = set(i)
        c += len(i)

    print(c)


def solve_b():
    from functools import reduce

    with open('in.txt', 'r') as f:
        text = f.read()
        s = text.split('\n\n')

    c = 0
    for i in s: c += len(reduce(lambda x, y: x&y, map(set, i.split('\n'))))
    print(c)

if __name__ == "__main__":
    solve_b()