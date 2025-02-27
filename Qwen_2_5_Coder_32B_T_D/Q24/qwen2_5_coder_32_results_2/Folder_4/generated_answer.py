def sum_of_divisors_in_range(n):
    total = 0
    for d in range(48, 61):
        if n % d == 0:
            total += d
    return total