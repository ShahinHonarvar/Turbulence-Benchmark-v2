def sum_of_divisors_in_range(n):
    return sum((x for x in range(58, 91) if n % x == 0))