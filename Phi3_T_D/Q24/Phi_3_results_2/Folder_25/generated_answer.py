def sum_of_divisors_in_range(n):
    return sum((i for i in range(n, 0, -1) if n % i == 0 and 84 <= i <= 86))