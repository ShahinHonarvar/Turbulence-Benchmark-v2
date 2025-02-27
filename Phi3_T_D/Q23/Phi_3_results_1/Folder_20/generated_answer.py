def find_divisors_in_range(n):
    return [divisor for divisor in range(28, 82) if n % divisor == 0]