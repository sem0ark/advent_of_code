def solve_ab():
    t = input()
    s = [0]*9
    for i in t.split(','):
        s[int(i)] += 1

    # n = 80 ## a
    n = 256 ## b

    for _ in range(n):
        to_birth = s[0]
        s[0:8] = s[1:9]
        s[8] = to_birth
        s[6] += to_birth

    print(sum(s))

if __name__ == "__main__":
    solve_ab()
