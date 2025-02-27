def find_divisors_in_range(n):
    result = [d for d in range(71, 82) if n % d == 0]
    return result