def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    divisors_sum = sum([i for i in range(378, 783) if n % i == 0])
    return divisors_sum