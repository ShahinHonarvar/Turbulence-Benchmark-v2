def sum_of_divisors_in_range(number):
    if number < 2:
        return 0
    sum_divisors = sum((divisor for divisor in range(2, min(number + 1, 7)) if number % divisor == 0))
    return sum_divisors