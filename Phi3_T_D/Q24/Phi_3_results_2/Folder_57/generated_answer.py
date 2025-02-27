def sum_of_divisors_in_range(n):
    divisors_sum = sum((i for i in range(1, n + 1) if n % i == 0 and 15 <= i <= 92))
    return divisors_sum