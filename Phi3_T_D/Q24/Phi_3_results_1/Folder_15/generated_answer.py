def sum_of_divisors_in_range(n):
    return sum((d for d in [i for i in range(1, n + 1) if n % i == 0] if 7 <= d <= 9))