def sum_of_divisors_in_range(num):
    divisors_sum = sum((i for i in range(48, 61) if num % i == 0))
    return divisors_sum