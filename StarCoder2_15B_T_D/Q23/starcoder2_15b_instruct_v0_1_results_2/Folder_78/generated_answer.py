def find_divisors_in_range(number):
    return [divisor for divisor in range(20, 51) if number % divisor == 0]