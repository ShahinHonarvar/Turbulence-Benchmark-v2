def sum_of_divisors_in_range(num):
    divisors_sum = sum((d for d in range(6, 9) if num % d == 0))
    return divisors_sum