def sum_of_divisors_in_range(n):
    if n < 1:
        raise ValueError('Input must be a positive integer')
    divisors = [d for d in range(45, 73) if n % d == 0]
    return sum(divisors)