def find_divisors_in_range(number):
    return [divisor for divisor in range(11, 57) if number % divisor == 0]