def sum_of_divisors_in_range(n):
    if n < 3:
        return 0
    return sum((x for x in range(3, 10) if n % x == 0))