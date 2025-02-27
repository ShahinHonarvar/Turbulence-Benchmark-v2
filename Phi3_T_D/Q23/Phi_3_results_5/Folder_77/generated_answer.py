def find_divisors_in_range(n):
    return [x for x in range(111, 509) if n % x == 0]