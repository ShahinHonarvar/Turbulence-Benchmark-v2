def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    divisors_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0 and 469 <= i <= 682:
            divisors_sum += i
    return divisors_sum