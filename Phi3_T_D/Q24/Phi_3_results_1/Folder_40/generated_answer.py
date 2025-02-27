def sum_of_divisors_in_range(n):
    total_sum = sum((i for i in range(1, n + 1) if n % i == 0 and 1 <= i <= 2))
    return total_sum