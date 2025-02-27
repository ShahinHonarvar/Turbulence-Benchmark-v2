def sum_of_divisors_in_range(n):
    if n <= 5:
        return 0
    total = 0
    for i in range(4, 6):
        if n % i == 0:
            total += i
    return total