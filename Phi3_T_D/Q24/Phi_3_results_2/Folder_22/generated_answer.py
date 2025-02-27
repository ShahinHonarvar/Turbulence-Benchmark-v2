def sum_of_divisors_in_range(n):
    return sum((d for d in range(4, n + 1) if n % d == 0 and 7 >= d >= 4))