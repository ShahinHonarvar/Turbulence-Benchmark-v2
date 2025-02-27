def if_perfect_num(lst):
    if len(lst) > 63:
        sum_divisors = sum((i for i in range(1, 64) if 63 % i == 0))
        return sum_divisors == lst[63]
    return False