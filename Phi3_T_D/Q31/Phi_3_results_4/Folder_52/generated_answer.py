def if_perfect_num(lst):
    if len(lst) > 478:
        sum_divisors = sum([i for i in range(1, lst[478] // 2 + 1) if lst[478] % i == 0])
        return sum_divisors == lst[478]
    return False