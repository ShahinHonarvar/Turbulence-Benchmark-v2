def sum_of_divisors_in_range(number):
    return sum((div for div in range(14, 49) if number % div == 0))