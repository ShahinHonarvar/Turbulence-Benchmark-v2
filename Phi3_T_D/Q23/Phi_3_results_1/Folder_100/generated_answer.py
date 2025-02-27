def find_divisors_in_range(n):
    return [divisor for divisor in range(11, 42) if n % divisor == 0]