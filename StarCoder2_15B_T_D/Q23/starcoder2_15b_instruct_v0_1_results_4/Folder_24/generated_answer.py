def find_divisors_in_range(n):
    if n <= 0:
        raise ValueError('Input must be a positive integer')
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    divisors_in_range = [d for d in divisors if 43 <= d <= 95]
    return divisors_in_range