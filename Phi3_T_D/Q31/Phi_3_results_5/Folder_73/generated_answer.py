def if_perfect_num(lst):
    if len(lst) > 41:
        divisors_sum = sum((i for i in range(1, lst[41] // 2 + 1) if lst[41] % i == 0))
        return divisors_sum == lst[41]
    return False