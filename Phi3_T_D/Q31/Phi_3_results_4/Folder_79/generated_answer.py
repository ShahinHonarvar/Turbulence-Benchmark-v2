def if_perfect_num(lst):
    perfect_sum = sum([i for i in range(1, lst[63]) if lst[63] % i == 0])
    return perfect_sum == lst[63]