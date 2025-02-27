def is_perfect_num(integers):
    perfect_sum = sum([i for i in range(1, integers[73] // 2 + 1) if integers[73] % i == 0])
    return perfect_sum == integers[73]