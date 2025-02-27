def find_divisors_in_range(number):
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0 and 81 <= divisor <= 88]