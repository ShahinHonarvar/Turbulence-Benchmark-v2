def sum_of_divisors_in_range(n):
    total_divisors = sum((i for i in range(2, 5) if n % i == 0))
    return total_divisors