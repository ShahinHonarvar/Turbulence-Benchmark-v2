def find_divisors_in_range(n):
    if n > 0:
        return [divisor for divisor in range(50, 85) if n % divisor == 0]
    else:
        return []