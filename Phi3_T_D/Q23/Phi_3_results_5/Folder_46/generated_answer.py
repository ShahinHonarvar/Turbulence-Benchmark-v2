def find_divisors_in_range(n):
    divisors = [divisor for divisor in range(81, 89) if n % divisor == 0]
    return divisors