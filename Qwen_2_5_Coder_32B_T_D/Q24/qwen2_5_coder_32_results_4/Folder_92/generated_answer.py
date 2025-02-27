def sum_of_divisors_in_range(n):
    if n < 9:
        return 0
    return 8 + 9 if 8 <= n // 8 <= 9 and 8 <= n // 9 <= 9 else 0