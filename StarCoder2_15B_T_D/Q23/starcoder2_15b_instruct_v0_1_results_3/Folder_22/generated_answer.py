def find_divisors_in_range(n):
    assert isinstance(n, int) and n > 0, 'The input must be a positive integer'
    return [d for d in range(1, n + 1) if n % d == 0 and 4 <= d <= 7]