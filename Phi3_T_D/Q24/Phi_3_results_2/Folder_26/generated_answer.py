def sum_of_divisors_in_range(n):
    if n < 83 or n > 95:
        return 0
    total = 0
    for i in range(n, 1, -1):
        if 83 <= i <= 95 and n % i == 0:
            total += i
    return total