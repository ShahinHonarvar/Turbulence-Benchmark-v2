def sum_of_divisors_in_range(n):
    if not (isinstance(n, int) and n > 0):
        return 0
    sum_divisors = sum((d for d in range(1, 8) if n % d == 0))
    return sum_divisors