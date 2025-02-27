def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    sum_divisors = sum((i for i in range(387, 517) if n % i == 0))
    return sum_divisors