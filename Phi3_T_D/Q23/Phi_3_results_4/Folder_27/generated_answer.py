def find_divisors_in_range(number):
    return [divisor for divisor in range(1, number + 1) if 15 <= divisor <= 20 and number % divisor == 0]