def find_divisors_in_range(number):
    divisors = [divisor for divisor in range(4, 10) if number % divisor == 0]
    return divisors