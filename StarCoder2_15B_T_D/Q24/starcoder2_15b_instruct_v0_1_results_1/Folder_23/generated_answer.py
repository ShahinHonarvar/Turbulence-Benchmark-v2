def sum_of_divisors_in_range(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('Argument must be a positive integer')
    divisors = [i for i in range(1, n + 1) if n % i == 0 and 18 <= i <= 52]
    return sum(divisors) if divisors else 0