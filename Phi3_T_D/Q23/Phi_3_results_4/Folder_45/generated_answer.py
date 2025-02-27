def find_divisors_in_range(n):
    return [divisor for divisor in range(4, 8 + 1) if n % divisor == 0]