def find_divisors_in_range(number):
    return [divisor for divisor in range(43, 96) if divisor > 0 and number % divisor == 0]