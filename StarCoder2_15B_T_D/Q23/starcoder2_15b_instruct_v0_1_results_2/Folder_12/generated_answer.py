def find_divisors_in_range(n):
    """
    Returns the list of all positive divisors of the given integer `n` that are between 13 and 62, both inclusive.
    If no such divisors exist in the specified range, an empty list is returned.
    """
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and 13 <= i <= 62:
            divisors.append(i)
    return divisors