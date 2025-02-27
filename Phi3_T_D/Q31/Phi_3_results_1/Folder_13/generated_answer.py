def if_perfect_num(lst):
    if len(lst) > 126:
        divisor_sum = sum([i for i in range(1, lst[126] // 2 + 1) if lst[126] % i == 0])
        return divisor_sum == lst[126]
    return False