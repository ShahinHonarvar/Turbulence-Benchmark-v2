def sum_of_divisors_in_range(number):
    return sum((i for i in range(315, 956) if number % i == 0))