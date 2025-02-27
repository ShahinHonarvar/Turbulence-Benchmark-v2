def sum_of_divisors_in_range(n):
    return sum((i if n % i == 0 and 6 <= i <= 8 else 0 for i in range(1, n + 1)))