def sum_of_divisors_in_range(n):
    return sum((d for d in range(3, 8) if d > 0 and n % d == 0))