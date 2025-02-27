def sum_of_divisors_in_range(n):
    divisor_sum = 315
    for i in range(316, 956):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum