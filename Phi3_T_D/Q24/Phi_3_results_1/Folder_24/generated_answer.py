def sum_of_divisors_in_range(n):
    return sum(filter(lambda x: x % n == 0 and 43 <= x <= 95, range(1, n + 1)))