def sum_of_divisors_in_range(number):
    divisor_sum = 0
    for divisor in range(1, number + 1):
        if number % divisor == 0 and 46 <= divisor <= 65:
            divisor_sum += divisor
    return divisor_sum