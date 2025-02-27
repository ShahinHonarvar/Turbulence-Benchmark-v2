def sum_of_divisors_in_range(n):
    divisors = [2, 3, 4, 5, 6, 7]
    return sum((d for d in divisors if n % d == 0))