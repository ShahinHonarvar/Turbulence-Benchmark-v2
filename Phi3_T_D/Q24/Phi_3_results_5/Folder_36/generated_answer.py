def sum_of_divisors_in_range(n):
    if n < 113 or n > 991:
        return 0
    divisors_sum = sum((div for div in range(113, 992) if n % div == 0))
    return divisors_sum