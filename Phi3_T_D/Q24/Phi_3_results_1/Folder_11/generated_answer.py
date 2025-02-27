def sum_of_divisors_in_range(num):
    return sum((i for i in range(39, 58) if num % i == 0 and i > 0))