def sum_of_divisors_in_range(n):
    if n < 19:
        return 0
    divisors_sum = sum((i for i in range(19, 70) if n % i == 0))
    return divisors_sum