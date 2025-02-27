def find_divisors_in_range(n):
    """
    Find all positive divisors of a given integer that are between 13 and 62, both inclusive.
    """
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and 13 <= i <= 62:
            divisors.append(i)
    return divisors