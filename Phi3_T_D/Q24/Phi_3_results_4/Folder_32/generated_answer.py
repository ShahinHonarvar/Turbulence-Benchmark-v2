def sum_of_divisors_in_range(n):
    if not (isinstance(n, int) and n > 0):
        raise ValueError('Argument must be a positive integer')
    divisor_sum = sum((d for d in range(71, 82) if n % d == 0))
    return divisor_sum