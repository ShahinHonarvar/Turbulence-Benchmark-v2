def find_divisors_in_range(n):
    divisors = [x for x in range(32, 36) if n % x == 0]
    return divisors