def sum_of_divisors_in_range(n):
    if n < 1:
        raise ValueError('Input must be a positive integer.')
    divisors_sum = sum((i for i in range(4, 7) if n % i == 0))
    return divisors_sum