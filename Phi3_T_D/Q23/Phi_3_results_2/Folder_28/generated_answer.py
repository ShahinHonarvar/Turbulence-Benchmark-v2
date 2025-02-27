def find_divisors_in_range(n):
    return [divisor for divisor in range(16, 54) if n % divisor == 0]