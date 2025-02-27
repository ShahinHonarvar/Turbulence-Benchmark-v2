def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(max(n // 378, 1), min(n // 782 + 1, n + 1)):
        if n % i == 0 and i >= 378 and (i <= 782):
            divisors_sum += i
    return divisors_sum