def find_divisors_in_range(n):
    return [d for d in range(120, 350) if d > 0 and n % d == 0]