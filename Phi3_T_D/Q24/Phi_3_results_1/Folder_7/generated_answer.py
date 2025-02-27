def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    divisor_sum = sum((i for i in range(469, 683) if n % i == 0))
    return divisor_sum