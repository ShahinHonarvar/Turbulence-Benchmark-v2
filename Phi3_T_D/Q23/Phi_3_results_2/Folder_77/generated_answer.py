def find_divisors_in_range(n):
    return [d for d in range(111, 509) if n % d == 0]