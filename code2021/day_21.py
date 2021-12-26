def roll_dice(n):
    n %= 100
    if n < 98: return (3*n+6)
    if n == 98: return 200
    if n == 99: return 103


def solve_a():
    a = int(input().split()[-1])-1
    b = int(input().split()[-1])-1
    
    score_a = 0
    score_b = 0

    i = 0
    while True:
        np = (a + roll_dice(i))%10
        score_a += np+1
        a = np
        # print(i, a+1, score_a)
        i += 3
        if score_a >= 1000:
            print(i*score_b)
            return
        np = (b + roll_dice(i))%10
        score_b += np+1
        b = np
        # print(i, b+1, score_b)
        i += 3
        if score_b >= 1000:
            print(i*score_a)
            return

def solve_b():
    from collections import defaultdict
    
    N = 21

    n_games = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]

    da = [[0]*22 for _ in range(20)]
    db = [[0]*22 for _ in range(20)]

    def dfs(p, s, n, games, d):
        if s < 21: d[n][s] += games
        else:
            d[n][21] += games
            return

        for k in range(3, 10):
            np = (p + k) % 10
            ns = s + np + 1
            dfs(np, ns, n+1, games*n_games[k], d)

    dfs(1-1, 0, 0, 1, da)
    dfs(6-1, 0, 0, 1, db)

    for i in da: print(i)
    for i in db: print(i)

    # compute a
    a = 0
    for turn in range(20): a += da[turn][21] * sum(db[turn-1][:21])
    # compute b
    b = 0
    for turn in range(20): b += db[turn][21] * sum(da[turn][:21])
    print(a, b)
    print(max(a, b))

if __name__ == "__main__":
    solve_b()


