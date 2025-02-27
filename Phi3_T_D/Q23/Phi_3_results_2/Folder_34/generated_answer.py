def find_divisors_in_range(n):
    return [divisor for divisor in range(4, min(n + 1, 6)) if n % divisor == 0]