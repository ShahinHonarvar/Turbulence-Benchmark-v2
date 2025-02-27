def find_divisors_in_range(n):
    result = [divisor for divisor in range(111, 509) if n % divisor == 0]
    return result