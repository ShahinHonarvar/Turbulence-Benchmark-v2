def sum_of_divisors_in_range(n):
    total = sum((d for d in range(28, 82) if n % d == 0))
    return total