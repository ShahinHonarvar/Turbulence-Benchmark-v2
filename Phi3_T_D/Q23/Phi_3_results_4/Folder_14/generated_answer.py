def find_divisors_in_range(number):
    divisors = [divisor for divisor in range(2, number + 1) if 6 <= divisor <= 8 and number % divisor == 0]
    return divisors