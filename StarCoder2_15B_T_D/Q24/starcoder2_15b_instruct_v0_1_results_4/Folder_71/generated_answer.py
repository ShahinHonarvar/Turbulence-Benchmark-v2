def sum_of_divisors_in_range(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError('The input must be a positive integer.')
    sum_of_divisors = 0
    for divisor in range(1, number + 1):
        if divisor >= 45 and divisor <= 72:
            sum_of_divisors += divisor
    return sum_of_divisors