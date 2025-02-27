def sum_of_divisors_in_range(n):
    divisors = [3, 4, 5, 6, 7]
    sum_divisors = 0
    for divisor in divisors:
        if n % divisor == 0:
            sum_divisors += divisor
    return sum_divisors