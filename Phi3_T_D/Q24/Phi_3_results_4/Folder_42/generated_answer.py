def sum_of_divisors_in_range(n):
    sum_divisors = 0
    divisor = 14
    while divisor <= 93:
        if n % divisor == 0:
            sum_divisors += divisor
        divisor += 1
    return sum_divisors