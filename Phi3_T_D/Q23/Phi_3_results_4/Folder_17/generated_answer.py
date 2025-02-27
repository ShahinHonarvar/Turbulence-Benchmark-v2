def find_divisors_in_range(number):
    return [divisor for divisor in range(10, 70) if number % divisor == 0]