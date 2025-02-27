def find_divisors_in_range(n):
    return [divisor for divisor in range(2, 8) if n % divisor == 0]