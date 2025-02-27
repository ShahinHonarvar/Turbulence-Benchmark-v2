def sum_of_divisors_in_range(n):
    divisor_sum = sum((i for i in range(4, 10) if n % i == 0))
    return divisor_sum