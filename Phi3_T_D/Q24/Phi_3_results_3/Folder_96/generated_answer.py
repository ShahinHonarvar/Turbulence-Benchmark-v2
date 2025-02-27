def sum_of_divisors_in_range(n):
    return sum((x for x in range(9, n) if n % x == 0 and 5 <= x < 9))