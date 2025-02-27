def sum_of_divisors_in_range(n):
    sum_divisors = sum([i for i in range(10, 56) if n % i == 0])
    return sum_divisors