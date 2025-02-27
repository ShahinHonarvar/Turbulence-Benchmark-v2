def find_divisors_in_range(n):
    return [divisor for divisor in range(32, 91) if n % divisor == 0]