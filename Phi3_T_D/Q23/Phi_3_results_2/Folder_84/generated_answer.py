def find_divisors_in_range(n):
    divisors_in_range = [divisor for divisor in range(224, 585) if n % divisor == 0]
    return divisors_in_range