def sum_of_divisors_in_range(n: int) -> int:
    divisors_in_range = [d for d in range(1, n + 1) if n % d == 0 and 4 <= d <= 8]
    if not divisors_in_range:
        return 0
    return sum(divisors_in_range)