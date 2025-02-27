def sum_of_divisors_in_range(n):
    sum_divisors = sum((x for x in range(3, 10) if n % x == 0))
    return sum_divisors