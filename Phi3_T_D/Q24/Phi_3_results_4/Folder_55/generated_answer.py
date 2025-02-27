def sum_of_divisors_in_range(n):
    return sum((i for i in range(5 if n >= 5 else 0, 9) if n % i == 0))