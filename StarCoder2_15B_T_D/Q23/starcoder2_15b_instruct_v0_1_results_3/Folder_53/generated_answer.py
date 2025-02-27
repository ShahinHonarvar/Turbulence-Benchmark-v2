def find_divisors_in_range(n):
    """Find all positive divisors of n that are between 4 and 9, both inclusive."""
    divisors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if 4 <= i <= 9:
                divisors.append(i)
            if 4 <= n // i <= 9:
                divisors.append(n // i)
    return divisors