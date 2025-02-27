def find_divisors_in_range(number):
    divisors = [divisor for divisor in range(39, 58) if divisor != 0 and number % divisor == 0]
    return divisors