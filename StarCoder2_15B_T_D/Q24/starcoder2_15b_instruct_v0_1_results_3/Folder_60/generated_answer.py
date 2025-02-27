def sum_of_divisors_in_range(number):
    total_sum = 0
    for divisor in range(1, number + 1):
        if number % divisor == 0 and 41 <= divisor <= 55:
            total_sum += divisor
    return total_sum