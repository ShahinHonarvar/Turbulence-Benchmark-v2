def sum_of_divisors_in_range(n):
    return sum([i for i in range(1, min(n, 3) + 1) if n % i == 0])