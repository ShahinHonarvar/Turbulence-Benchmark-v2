def find_divisors_in_range(number):
    return [divisor for divisor in range(50, 82) if divisor != 0 and number % divisor == 0]