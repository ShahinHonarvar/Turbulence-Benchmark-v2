def sum_of_divisors_in_range(n):
    return sum((i for i in range(392, 466) if n % i == 0))