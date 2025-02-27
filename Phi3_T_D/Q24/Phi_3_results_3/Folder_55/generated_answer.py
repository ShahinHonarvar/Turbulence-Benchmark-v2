def sum_of_divisors_in_range(n):
    sum_divisors = sum((i for i in range(1, n + 1) if 5 <= i <= 8 and n % i == 0))
    return sum_divisors