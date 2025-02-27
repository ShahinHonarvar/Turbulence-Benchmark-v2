def find_divisors_in_range(n):
    divisors_in_range = [divisor for divisor in range(1, n + 1) if n % divisor == 0 and 16 <= divisor <= 53]
    return divisors_in_range