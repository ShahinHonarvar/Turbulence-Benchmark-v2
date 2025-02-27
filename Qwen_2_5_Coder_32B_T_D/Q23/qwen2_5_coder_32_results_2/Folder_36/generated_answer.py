def find_divisors_in_range(n):
    return [d for d in range(113, 992) if n % d == 0]