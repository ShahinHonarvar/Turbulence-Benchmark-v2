def sum_of_divisors_in_range(n: int) -> int:
    """
    Returns the sum of all positive divisors of the given integer that are between 48 and 62, both inclusive.
    If no such divisors exist in the specified range, returns 0.
    """
    divisors = [d for d in range(1, n + 1) if n % d == 0]
    sum_of_divisors = sum([d for d in divisors if 48 <= d <= 62])
    return sum_of_divisors