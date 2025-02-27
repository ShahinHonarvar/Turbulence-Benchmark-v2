def sum_of_divisors_in_range(n):
    sum_divisors = sum([i for i in range(3, 8) if n % i == 0])
    return sum_divisors