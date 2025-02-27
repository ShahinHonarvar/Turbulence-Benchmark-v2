def sum_of_divisors_in_range(n):
    divisors = [3, 4, 5]
    return sum((x for x in divisors if n % x == 0))