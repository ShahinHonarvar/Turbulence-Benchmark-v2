def sum_of_divisors_in_range(num):
    return sum((i for i in range(113, 992) if num % i == 0))