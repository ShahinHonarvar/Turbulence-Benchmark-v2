def sum_of_divisors_in_range(n):
    return sum([i for i in range(2, 4) if n % i == 0])