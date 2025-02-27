def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    sum_of_divisors = 0
    for divisor in divisors:
        if 2 <= divisor <= 4:
            sum_of_divisors += divisor
    return sum_of_divisors