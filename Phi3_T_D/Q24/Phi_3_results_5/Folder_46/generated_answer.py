def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    return sum((d for d in range(81, 89) if n % d == 0))