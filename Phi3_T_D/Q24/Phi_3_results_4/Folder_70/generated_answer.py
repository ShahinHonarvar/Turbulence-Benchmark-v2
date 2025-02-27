def sum_of_divisors_in_range(n):
    return sum((i for i in range(586, 841) if n % i == 0)) if n > 0 else 0