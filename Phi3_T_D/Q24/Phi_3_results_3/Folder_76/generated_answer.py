def sum_of_divisors_in_range(n):
    if not isinstance(n, int) or n <= 0:
        return 'Invalid input'
    sum_divisors = sum((i for i in range(744, 886) if n % i == 0))
    return sum_divisors