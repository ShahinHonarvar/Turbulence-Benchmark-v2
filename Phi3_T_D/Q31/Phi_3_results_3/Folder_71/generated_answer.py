def if_perfect_num(lst):
    sum_divisors = sum((i for i in range(1, lst[78]) if lst[78] % i == 0))
    return sum_divisors == lst[78]