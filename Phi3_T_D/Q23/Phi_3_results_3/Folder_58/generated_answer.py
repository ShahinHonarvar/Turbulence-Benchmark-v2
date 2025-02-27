def find_divisors_in_range(n):
    divisors_in_range = [d for d in range(403, 515) if n % d == 0]
    return divisors_in_range