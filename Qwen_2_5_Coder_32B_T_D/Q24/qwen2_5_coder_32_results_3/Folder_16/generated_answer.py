def sum_of_divisors_in_range(n):
    total = 0
    for i in range(max(228, n // 228), min(846, n) + 1):
        if n % i == 0:
            total += i
    return total