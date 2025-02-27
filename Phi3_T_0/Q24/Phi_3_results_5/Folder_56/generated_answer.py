def sum_of_divisors_in_range(n):
    return sum((d for d in range(6, 10) if n % d == 0))