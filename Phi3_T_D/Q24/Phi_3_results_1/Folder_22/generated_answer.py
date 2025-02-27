def sum_of_divisors_in_range(n):
    sum_divisors = sum((divisor for divisor in range(4, 8) if n % divisor == 0))
    return sum_divisors