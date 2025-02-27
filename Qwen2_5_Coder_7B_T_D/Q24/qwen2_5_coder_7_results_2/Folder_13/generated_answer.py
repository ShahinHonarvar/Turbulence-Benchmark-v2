def sum_of_divisors_in_range(n):
    return sum((d for d in range(472, 828) if n % d == 0))