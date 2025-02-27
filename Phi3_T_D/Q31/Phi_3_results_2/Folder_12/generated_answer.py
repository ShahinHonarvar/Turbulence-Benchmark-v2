def if_perfect_num(lst):
    if len(lst) > 27:
        divisor_sum = sum([i for i in range(1, lst[27]) if lst[27] % i == 0])
        return divisor_sum == lst[27]
    return False