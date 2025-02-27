def find_divisors_in_range(n):
    return [divisor for divisor in range(157, 903) if n % divisor == 0]