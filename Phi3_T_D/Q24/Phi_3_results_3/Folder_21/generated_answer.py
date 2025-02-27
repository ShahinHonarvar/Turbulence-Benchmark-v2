def sum_of_divisors_in_range(number):
    divisor_sum = sum((i for i in range(120, 350) if number % i == 0))
    return divisor_sum