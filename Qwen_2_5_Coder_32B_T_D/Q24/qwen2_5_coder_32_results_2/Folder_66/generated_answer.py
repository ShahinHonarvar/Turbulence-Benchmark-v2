def sum_of_divisors_in_range(n):
    r = [d for d in range(32, 36) if n % d == 0]
    return sum(r) if r else 0