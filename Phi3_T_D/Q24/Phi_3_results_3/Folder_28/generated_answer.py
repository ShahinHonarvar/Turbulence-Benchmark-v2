def sum_of_divisors_in_range(number):
    divisors_sum = 0
    for i in range(16, 54):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum