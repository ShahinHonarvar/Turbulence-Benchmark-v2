def sum_of_divisors_in_range(n):
    if n > 0:
        divisors = [d for d in range(1, n + 1) if n % d == 0 and d >= 461 and (d <= 827)]
        return sum(divisors)
    else:
        return 0