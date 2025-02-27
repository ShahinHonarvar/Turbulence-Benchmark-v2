def find_divisors_in_range(n):
    if n < 2:
        return []
    return [d for d in range(2, 5) if n % d == 0]