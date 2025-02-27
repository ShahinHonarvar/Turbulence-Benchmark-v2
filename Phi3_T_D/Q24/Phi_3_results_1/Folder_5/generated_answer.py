def sum_of_divisors_in_range(number):
    divisors_sum = sum((d for d in range(7, 9) if number % d == 0))
    return divisors_sum