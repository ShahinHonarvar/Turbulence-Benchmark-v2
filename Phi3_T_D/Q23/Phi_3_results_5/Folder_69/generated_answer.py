def find_divisors_in_range(number):
    return [divisor for divisor in range(658, 869) if divisor != 0 and number % divisor == 0]