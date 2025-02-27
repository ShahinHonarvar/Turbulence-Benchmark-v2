def find_divisors_in_range(n):
    if n <= 1:
        raise ValueError('Input must be a positive integer greater than 1')
    return [i for i in range(2, 5) if n % i == 0]