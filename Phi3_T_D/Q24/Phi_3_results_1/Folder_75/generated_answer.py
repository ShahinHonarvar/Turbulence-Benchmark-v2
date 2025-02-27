def sum_of_divisors_in_range(n):
    if n < 2:
        return 0
    return sum((i for i in range(38, 66) if n % i == 0))