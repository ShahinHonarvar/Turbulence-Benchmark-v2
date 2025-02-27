def sum_of_divisors_in_range(num):
    if num < 71:
        return 0
    return sum((i for i in range(71, 82) if num % i == 0))