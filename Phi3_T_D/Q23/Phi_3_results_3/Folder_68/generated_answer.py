def find_divisors_in_range(n):
    return [divisor for divisor in range(3, 7) if divisor != 0 and n % divisor == 0]