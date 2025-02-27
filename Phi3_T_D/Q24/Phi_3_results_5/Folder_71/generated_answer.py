def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    divisors_sum = 0
    for i in range(n, 0, -1):
        if n % i == 0 and 45 <= i <= 72:
            divisors_sum += i
    return divisors_sum