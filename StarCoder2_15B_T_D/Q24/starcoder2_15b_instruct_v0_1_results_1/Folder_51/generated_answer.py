def sum_of_divisors_in_range(num):
    return sum((d for d in range(2, 8) if num % d == 0))