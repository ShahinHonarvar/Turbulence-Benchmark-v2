def sum_of_divisors_in_range(num):
    divisor_sum = 0
    divisor = 6
    while divisor <= 7:
        if num % divisor == 0:
            divisor_sum += divisor
        divisor += 1
    return divisor_sum