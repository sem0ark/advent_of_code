def solve_a():

    with open('in.txt', 'r') as f:
        text = f.read()
        s = text.split('\n\n')

    good = {'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid',
    }

    count_valid = 0

    for passport in s:
        passport = passport.replace('\n', ' ')
        passport = passport.split(' ')
        d = set()
        for field in passport:
            d.add(field.split(':')[0])
        if len(good.intersection(d)) == len(good):
            count_valid += 1

    print(count_valid)



def solve_b():
    import re

    with open('in.txt', 'r') as f:
        text = f.read()
        s = text.split('\n\n')

    good = {'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid',
    }

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193.
    #   If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    def check_pass(passport):
        if not(re.match(r'^[\d]{4}$', passport['byr']) and 1920<=int(passport['byr'])<=2002): return False
        if not(re.match(r'^[\d]{4}$', passport['iyr']) and 2010<=int(passport['iyr'])<=2020): return False
        if not(re.match(r'^[\d]{4}$', passport['eyr']) and 2020<=int(passport['eyr'])<=2030): return False
        if not(re.match(r'^\#[\da-f]{6}$', passport['hcl'])): return False
        if not(passport['ecl'] in 'amb blu brn gry grn hzl oth'.split()): return False
        if not(re.match(r'^[\d]{9}$', passport['pid'])): return False

        if not(re.match(r'^([\d]+)(in|cm)$', passport['hgt'])): return False
        t = re.match(r'^([\d]+)(in|cm)$', passport['hgt']).groups()
        if t[1] == 'in' and not(59<=int(t[0])<=76): return False
        if t[1] == 'cm' and not(150<=int(t[0])<=193): return False

        return True

    count_valid = 0

    for passport in s:
        passport = passport.replace('\n', ' ')
        passport = passport.split(' ')
        d = {}
        for field in passport:
            a, b = field.split(':')
            d[a] = b
        if len(good.intersection(d)) == len(good) and check_pass(d):
            count_valid += 1

    print(count_valid)

if __name__ == "__main__":
    solve_b()