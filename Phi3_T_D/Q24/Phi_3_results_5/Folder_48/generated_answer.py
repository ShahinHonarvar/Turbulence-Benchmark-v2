def sum_of_divisors_in_range(n):
    if n < 1:
        raise ValueError('Input must be a positive integer')
    divisors_sum = sum((d for d in range(461, 828) if n % d == 0))
    return divisors_sum