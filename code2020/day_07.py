def solve_a():
    import re
    from collections import defaultdict

    with open('in.txt', 'r') as f: s = f.readlines()

    tree_bags = {}

    pat = re.compile(r'^([\w\s]+) bags contain ([\D\d]+)\.$')

    for rule in s:
        m = re.match(pat, rule)
        parent, childs = m.groups()
        tree_bags[parent] = re.findall(r'[\d]+ ([\w\s]+) bag', childs)

    # for i in tree_bags.items():
    #     print(i)

    have_gold = set()

    def dfs(cur):
        if cur in have_gold: return True
        t = False
        for i in tree_bags[cur]:
            t = t or (i == 'shiny gold') or dfs(i)
        if t: have_gold.add(cur)
        return t

    for i in tree_bags.keys(): dfs(i)

    print(len(have_gold))



def solve_b():
    import re
    from collections import defaultdict

    with open('in.txt', 'r') as f: s = f.readlines()

    tree_bags = {}

    pat = re.compile(r'^([\w\s]+) bags contain ([\D\d]+)\.$')

    for rule in s:
        m = re.match(pat, rule)
        parent, childs = m.groups()
        tree_bags[parent] = re.findall(r'([\d]+) ([\w\s]+) bag', childs)

    # for i in tree_bags.items():
    #     print(i)

    def dfs(cur):
        if not tree_bags[cur]: return 1
        res = 1
        for i in tree_bags[cur]: res += int(i[0])*dfs(i[1])
        return res

    print(dfs('shiny gold')-1)


if __name__ == "__main__":
    solve_b()