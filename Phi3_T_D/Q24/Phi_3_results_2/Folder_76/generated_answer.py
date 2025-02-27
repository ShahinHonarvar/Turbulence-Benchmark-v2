def sum_of_divisors_in_range(n):
    sum_of_divisors = sum((i for i in range(744, 886) if n % i == 0))
    return sum_of_divisors