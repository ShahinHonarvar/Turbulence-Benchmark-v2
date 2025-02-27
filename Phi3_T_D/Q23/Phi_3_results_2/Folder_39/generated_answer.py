def find_divisors_in_range(n):
    return [divisor for divisor in range(11, min(n, 57)) if n % divisor == 0]