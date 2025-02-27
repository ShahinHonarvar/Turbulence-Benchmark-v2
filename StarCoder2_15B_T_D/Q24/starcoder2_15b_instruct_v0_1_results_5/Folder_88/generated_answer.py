def sum_of_divisors_in_range(num):
    return sum((d for d in range(6, 8) if num % d == 0))