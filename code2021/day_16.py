def solve_a():
    hex_input = input()

    bits = ''

    for i in hex_input:
        cur = bin(int(i, 16))[2:]
        cur = '0'*(4-len(cur))+cur
        bits += cur


    ver_sum = [0]

    def parse_literal(p):
        res_num = ''
        while True:
            res_num += bits[p+1:p+5]
            p += 5
            if bits[p-5] == '0': break
        return int(res_num, 2), p

    def parse_inner_wlength(p):
        length = int(bits[p:p+15], 2)
        p += 15
        st_p = p
        while p-st_p < length:
            p = parse_packet(p)
        return p

    def parse_inner_wnum(p):
        length = int(bits[p:p+11], 2)
        p += 11
        for _ in range(length):
            p = parse_packet(p)
        return p

    def parse_packet(p):
        version = int(bits[p:p+3], 2)
        p += 3
        type_id = int(bits[p:p+3], 2)
        p += 3

        if type_id == 4:
            num, p = parse_literal(p)
            print('current: ', version, num, p)
        else:
            length_type = int(bits[p], 2)
            p += 1
            if length_type == 0: p = parse_inner_wlength(p)
            if length_type == 1: p = parse_inner_wnum(p)
            print('current: ', version, None, p)
        
        ver_sum[0] += version

        return p

    parse_packet(0)
    print(ver_sum)
    

def solve_b():
    hex_input = input()

    bits = ''

    for i in hex_input:
        cur = bin(int(i, 16))[2:]
        cur = '0'*(4-len(cur))+cur
        bits += cur


    def evaluate_expr(type_id, nums):
        if type_id == 0: return sum(nums)
        if type_id == 1:
            res = 1
            for i in nums: res *= i
            return res
        if type_id == 2: return min(nums)
        if type_id == 3: return max(nums)
        if type_id == 5: return int(nums[0] > nums[1])
        if type_id == 6: return int(nums[0] < nums[1])
        if type_id == 7: return int(nums[0] == nums[1])

    def parse_literal(p):
        res_num = ''
        while True:
            res_num += bits[p+1:p+5]
            p += 5
            if bits[p-5] == '0': break
        return int(res_num, 2), p

    def parse_inner_wlength(p, type_id):
        length = int(bits[p:p+15], 2)
        p += 15
        st_p = p
        nums = []
        while p-st_p < length:
            val, p = parse_packet(p)
            nums += [val]
        res = evaluate_expr(type_id, nums)
        return res, p

    def parse_inner_wnum(p, type_id):
        length = int(bits[p:p+11], 2)
        p += 11
        nums = []
        for _ in range(length):
            val, p = parse_packet(p)
            nums += [val]
        res = evaluate_expr(type_id, nums)
        return res, p

    def parse_packet(p):
        version = int(bits[p:p+3], 2)
        p += 3
        type_id = int(bits[p:p+3], 2)
        p += 3

        val = 0

        if type_id == 4:
            val, p = parse_literal(p)
            print('current: ', version, val, p)
        else:
            length_type = int(bits[p], 2)
            p += 1
            if length_type == 0: val, p = parse_inner_wlength(p, type_id)
            if length_type == 1: val, p = parse_inner_wnum(p, type_id)
            print('current: ', version, val, p)

        return val, p

    
    print(parse_packet(0))

if __name__ == "__main__":
    solve_b()

