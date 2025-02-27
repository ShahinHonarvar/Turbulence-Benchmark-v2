def find_divisors_in_range(number):
    return [divisor for divisor in range(1, number + 1) if divisor % number == 0 and 35 <= divisor <= 37]