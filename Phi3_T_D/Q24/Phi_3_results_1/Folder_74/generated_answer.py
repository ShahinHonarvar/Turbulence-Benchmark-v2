def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for potential_divisor in range(40, 75):
        if n % potential_divisor == 0:
            divisors_sum += potential_divisor
    return divisors_sum