from collections import defaultdict

def solve_a():
    t = input()
    graph = defaultdict(list)
    while len(t)>0:
        a, b = t.split('-')
        graph[a].append(b)
        graph[b].append(a)
        t = input()

    count = [0]

    def dfs(cur, used):
        if cur == 'end':
            count[0] += 1
            return

        for nxt in graph[cur]:
            if nxt.islower() and nxt in used: continue
            dfs(nxt, used+[nxt])

    dfs('start', ['start'])

    print(count[0])

def solve_b():
    t = input()
    graph = defaultdict(list)
    while len(t)>0:
        a, b = t.split('-')
        graph[a].append(b)
        graph[b].append(a)
        t = input()

    count = [0]

    def dfs(cur, used, used_twice):
        if cur == 'end':
            count[0] += 1
            return

        for nxt in graph[cur]:
            if nxt == 'start': continue
            if nxt.islower():
                if nxt in used:
                    if used_twice: continue
                    else: dfs(nxt, used+[nxt], True)
                else: dfs(nxt, used+[nxt], used_twice)
            else: dfs(nxt, used+[nxt], used_twice)

    dfs('start', ['start'], False)

    print(count[0])

if __name__ == "__main__":
    solve_b()