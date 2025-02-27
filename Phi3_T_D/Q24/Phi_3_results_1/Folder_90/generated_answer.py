def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for i in range(n, 0, -1):
        if n % i == 0 and 451 <= i <= 973:
            divisor_sum += i
    return divisor_sum