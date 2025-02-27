def find_divisors_in_range(n):
    if n < 1:
        raise ValueError('Input must be a positive integer')
    divisors = [d for d in range(469, 683) if n % d == 0]
    return divisors