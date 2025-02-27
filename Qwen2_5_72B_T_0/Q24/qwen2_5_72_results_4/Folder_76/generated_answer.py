def sum_of_divisors_in_range(n):
    total = 0
    for i in range(744, 886):
        if n % i == 0:
            total += i
    return total