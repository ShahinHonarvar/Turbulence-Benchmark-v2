def sum_of_divisors_in_range(number):
    return sum((divisor for divisor in range(14, 94) if divisor > 0 and number % divisor == 0))