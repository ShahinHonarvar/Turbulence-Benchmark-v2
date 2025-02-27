def find_divisors_in_range(n):
    return [divisor for divisor in range(1, n + 1) if n % divisor == 0 and 4 <= divisor <= 6]