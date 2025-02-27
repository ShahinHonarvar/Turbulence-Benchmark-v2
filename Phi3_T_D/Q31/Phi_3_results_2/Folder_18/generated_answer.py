def is_perfect_num(lst):
    if len(lst) > 312:
        n = lst[312]
        factors = [i for i in range(1, n) if n % i == 0]
        return sum(factors) == n
    return False