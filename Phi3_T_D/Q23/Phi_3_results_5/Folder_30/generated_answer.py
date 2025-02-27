def find_divisors_in_range(number):
    divisors = [divisor for divisor in range(42, 78) if number % divisor == 0]
    return divisors