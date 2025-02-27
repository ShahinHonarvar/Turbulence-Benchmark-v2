def sum_of_divisors_in_range(n):
    divisors_sum = sum((i for i in range(16, 69) if n % i == 0))
    return divisors_sum