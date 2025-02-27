def sum_of_divisors_in_range(n):
    if n < 5:
        return 0
    return 4 + 5 if 5 <= n else 4 if 4 <= n else 0