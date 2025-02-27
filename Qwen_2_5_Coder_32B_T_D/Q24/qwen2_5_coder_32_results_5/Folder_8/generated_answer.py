def sum_of_divisors_in_range(n):
    return sum((x for x in range(48, 63) if n % x == 0))