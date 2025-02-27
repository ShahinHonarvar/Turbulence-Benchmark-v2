def sum_of_divisors_in_range(number):
    return sum((divisor for divisor in range(43, 47) if number % divisor == 0))