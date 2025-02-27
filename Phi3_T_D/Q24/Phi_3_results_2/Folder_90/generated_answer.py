def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    divisor_sum = 0
    for i in range(451, min(973 + 1, n ** 0.5 + 1)):
        if n % i == 0:
            if 451 <= i <= n:
                divisor_sum += i
            j = n // i
            if 451 <= j <= n and j != i:
                divisor_sum += j
    return divisor_sum