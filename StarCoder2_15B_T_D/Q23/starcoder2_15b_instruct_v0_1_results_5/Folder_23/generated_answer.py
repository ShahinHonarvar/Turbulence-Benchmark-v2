def find_divisors_in_range(number):
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0 and 18 <= divisor <= 52]