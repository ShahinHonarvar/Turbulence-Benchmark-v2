def sum_of_divisors_in_range(n):
    return sum((d for d in range(3, n + 1) if n % d == 0 and 3 <= d <= 8))