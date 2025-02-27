def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    sum_divisors = sum((i for i in range(42, 78) if n % i == 0))
    return sum_divisors