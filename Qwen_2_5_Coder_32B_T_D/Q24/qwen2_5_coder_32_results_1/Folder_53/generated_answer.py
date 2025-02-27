def sum_of_divisors_in_range(n):
    divisors = [5, 6, 7, 8, 9]
    return sum((x for x in divisors if n % x == 0))