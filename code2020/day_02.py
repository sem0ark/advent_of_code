def solve_a():
    s = []
    t = input()
    while len(t)>0:
        s.append(t)
        t = input()

    count_valid = 0

    for string in s:
        low, hig = map(int, string.split()[0].split('-'))
        char = string.split()[1][0]
        password = string.split()[2]
        if low <= password.count(char) <= hig:
            count_valid += 1

    print(count_valid)

def solve_b():
    s = []
    t = input()
    while len(t)>0:
        s.append(t)
        t = input()

    count_valid = 0

    for string in s:
        a, b = map(int, string.split()[0].split('-'))
        char = string.split()[1][0]
        password = string.split()[2]
        count = (password[a-1]==char)*1 + (password[b-1]==char)*1
        if count==1:
            count_valid += 1

    print(count_valid)


if __name__ == "__main__":
    solve_b()