def sum_of_divisors_in_range(n):
    sum_of_divisors = 0
    for divisor in range(1, n + 1):
        if n % divisor == 0 and 228 <= divisor <= 846:
            sum_of_divisors += divisor
    return sum_of_divisors