def sum_of_divisors_in_range(number):
    return sum((x for x in range(16, 69) if number % x == 0))