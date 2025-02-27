def if_perfect_num(lst):
    if len(lst) < 93:
        return False
    n = lst[92]
    sum_factors = sum((i for i in range(1, n) if n % i == 0))
    return sum_factors == n