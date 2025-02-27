def sum_of_divisors_in_range(number):
    divisor_sum = 0
    for i in range(15, 93):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum