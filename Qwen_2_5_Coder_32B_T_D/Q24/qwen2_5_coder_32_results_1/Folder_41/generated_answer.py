def sum_of_divisors_in_range(n):
    if n < 2:
        return 0
    sum_divisors = 0
    for divisor in range(2, 5):
        if n % divisor == 0:
            sum_divisors += divisor
    return sum_divisors