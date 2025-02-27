def find_divisors_in_range(n):
    divisors = [d for d in range(27, 45) if n % d == 0]
    return divisors