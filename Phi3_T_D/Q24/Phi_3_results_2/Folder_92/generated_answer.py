def sum_of_divisors_in_range(n):
    divisors_sum = sum((d for d in range(8, 10) if n % d == 0))
    return divisors_sum