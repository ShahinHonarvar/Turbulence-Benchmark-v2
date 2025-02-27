def sum_of_divisors_in_range(n):
    return sum((d for d in range(3, 5) if n % d == 0))