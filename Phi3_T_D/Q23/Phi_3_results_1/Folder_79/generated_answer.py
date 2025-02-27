def find_divisors_in_range(number):
    return [divisor for divisor in range(1, 9) if number % divisor == 0]