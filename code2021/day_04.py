import pprint as pp

def solve_a():
    GRID_SIZE = 5

    with open('in.txt', 'r') as f:
        nums = list(map(int, f.readline().split(',')))

        boards = f.read().strip('\n').split('\n\n')
        for ind in range(len(boards)):
            board = boards[ind]
            board = [[int(j) for j in i.split() if j] for i in board.split('\n')]
            boards[ind] = board

    def compute_bingo(grid, nums):
        row_counter = [0]*GRID_SIZE
        col_counter = [0]*GRID_SIZE
        # pp.pprint(grid)
        c = 0
        while c < len(nums):
            cur = nums[c]
            try:
                y = -1
                for i in range(GRID_SIZE):
                    if cur in grid[i]:
                        y = i
                if y >= 0:
                    row_counter[y] += 1
                    col_counter[grid[y].index(cur)] += 1
            except IndexError: pass
            # print(c)
            # pp.pprint(row_counter)
            # pp.pprint(col_counter)
            
            if any(i==GRID_SIZE for i in row_counter) or \
                any(i==GRID_SIZE for i in col_counter):
                return c
            c += 1
        return c

    def get_res(grid, nums, c):
        from functools import reduce
        s = reduce(lambda x, y: x|y, [set(i) for i in grid])
        for i in range(c+1):
            s.discard(nums[i])

        return sum(s)*nums[c]

    best_a = (1000000,0)
    best_b = (0,0)
    for i in range(len(boards)):
        last_ind = compute_bingo(boards[i], nums)
        best_a = min(best_a, (last_ind, i))
        best_b = max(best_b, (last_ind, i))

    print(get_res(boards[best_a[1]], nums, best_a[0]))
    print(get_res(boards[best_b[1]], nums, best_b[0]))


if __name__ == "__main__":
    solve_a()

