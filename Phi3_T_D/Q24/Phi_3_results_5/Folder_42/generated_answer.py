def sum_of_divisors_in_range(n):
    divisors = [d for d in range(1, n + 1) if n % d == 0 and 14 <= d <= 93]
    return sum(divisors)