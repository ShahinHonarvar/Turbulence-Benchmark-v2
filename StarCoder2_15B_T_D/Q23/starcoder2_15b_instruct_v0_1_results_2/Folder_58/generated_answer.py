def find_divisors_in_range(n):
    return [d for d in range(1, n + 1) if n % d == 0 and 403 <= d <= 514]