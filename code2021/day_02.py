def solve_a():
    t = input()

    x_pos = 0
    depth = 0
    
    while t:
        ch, d = t.split()
        if ch == 'forward':
            x_pos += int(d)
        elif ch == 'up':
            depth -= int(d)
        elif ch == 'down':
            depth += int(d)
        t = input()

    print(x_pos*depth)

def solve_b():
    t = input()

    x_pos = 0
    depth = 0
    aim = 0
    
    while t:
        ch, d = t.split()
        if ch == 'forward':
            x_pos += int(d)
            depth += aim*int(d)
        elif ch == 'up':
            aim -= int(d)
        elif ch == 'down':
            aim += int(d)
        t = input()

    print(x_pos*depth)

if __name__ == "__main__":
    solve_b()