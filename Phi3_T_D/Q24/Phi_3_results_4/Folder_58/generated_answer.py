def sum_of_divisors_in_range(n):
    sum_of_divisors = sum((d for d in range(403, 515) if n % d == 0))
    return sum_of_divisors