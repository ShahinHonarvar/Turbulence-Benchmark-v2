def sum_of_divisors_in_range(n):
    if n < 120 or n > 349:
        return 0
    divisors_sum = sum((i for i in range(120, 350) if n % i == 0))
    return divisors_sum