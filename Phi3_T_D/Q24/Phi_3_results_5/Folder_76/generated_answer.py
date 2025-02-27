def sum_of_divisors_in_range(number):
    return sum((i for i in range(744, 886) if number % i == 0))