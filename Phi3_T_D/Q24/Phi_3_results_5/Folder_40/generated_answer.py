def sum_of_divisors_in_range(n):
    sum_divisors = sum((d for d in range(1, 3) if n % d == 0))
    return sum_divisors