def sum_of_divisors_in_range(n):
    if n < 157:
        return 0
    summ = sum((d for d in range(157, min(n + 1, 903)) if n % d == 0))
    return summ