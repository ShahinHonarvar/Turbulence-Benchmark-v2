def sum_of_divisors_in_range(number):
    return sum((divisor for divisor in range(42, 78) if number % divisor == 0))