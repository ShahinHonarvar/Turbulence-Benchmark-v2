def sum_of_divisors_in_range(n):
    total_sum = sum((i for i in range(18, 53) if n % i == 0))
    return total_sum