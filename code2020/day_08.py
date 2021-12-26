def solve_a():
    commands = []
    t = input()
    while t:
        c, d = t.split()
        commands.append((c, int(d)))
        t = input()

    used = set()
    cur = 0
    acc = 0
    while cur not in used and cur < len(commands):
        used.add(cur)
        c, d = commands[cur]
        if c == 'acc':
            acc += d
            cur += 1
        elif c == 'nop':
            cur += 1
        elif c == 'jmp':
            cur += d

    print(acc)
    return cur, acc

def run(commands):
    used = set()
    cur = 0
    acc = 0
    while cur not in used and cur < len(commands):
        used.add(cur)
        c, d = commands[cur]
        if c == 'acc':
            acc += d
            cur += 1
        elif c == 'nop':
            cur += 1
        elif c == 'jmp':
            cur += d
    
    return cur, acc

def solve_b():
    commands = []
    to_change = []
    t = input()
    i = 0
    while t:
        c, d = t.split()
        commands.append((c, int(d)))
        if c in ['nop', 'jmp']: to_change.append(i)
        t = input()
        i += 1

    for change_ind in to_change:
        com = commands[change_ind]
        if com[0] == 'nop': commands[change_ind] = ('jmp', com[1])
        if com[0] == 'jmp': commands[change_ind] = ('nop', com[1])

        res_ind, acc = run(commands)
        if res_ind == len(commands): print(acc)
        commands[change_ind] = com

if __name__ == "__main__":
    solve_b()
