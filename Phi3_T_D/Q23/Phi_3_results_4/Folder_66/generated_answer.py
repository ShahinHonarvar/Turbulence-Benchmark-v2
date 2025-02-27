def find_divisors_in_range(number):
    return [divisor for divisor in range(32, 36) if divisor > 0 and number % divisor == 0]