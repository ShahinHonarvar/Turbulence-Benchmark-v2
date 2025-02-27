def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    sum_divisors = 0
    for possible_divisor in range(111, 509):
        if n % possible_divisor == 0:
            sum_divisors += possible_divisor
    return sum_divisors