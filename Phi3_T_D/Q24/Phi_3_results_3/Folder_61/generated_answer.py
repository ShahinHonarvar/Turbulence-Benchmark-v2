def sum_of_divisors_in_range(n):
    return sum((i for i in range(2, min(n + 1, 4)) if n % i == 0))