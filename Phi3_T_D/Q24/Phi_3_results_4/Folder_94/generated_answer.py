def sum_of_divisors_in_range(n):
    result = sum((d for d in range(35, 38) if n % d == 0))
    return result