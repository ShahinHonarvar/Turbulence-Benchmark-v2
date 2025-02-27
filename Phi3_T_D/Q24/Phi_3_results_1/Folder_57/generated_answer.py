def sum_of_divisors_in_range(number):
    return sum((divisor for divisor in range(15, 93) if number % divisor == 0))