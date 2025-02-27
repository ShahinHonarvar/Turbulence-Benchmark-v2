def sum_of_divisors_in_range(n):
    return sum((d for d in range(11, n + 1) if n % d == 0 and 41 >= d >= 11))