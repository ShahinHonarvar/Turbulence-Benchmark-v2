def sum_of_divisors_in_range(n):
    return sum((d for d in range(n, -1, -1) if n % d == 0 and 70 <= d <= 93))