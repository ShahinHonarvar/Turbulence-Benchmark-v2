def find_divisors_in_range(n):
    """
    Returns the list of all positive divisors of the given integer `n`
    that are between 4 and 6, both inclusive.
    If no such divisors exist in the specified range, returns an empty list.
    """
    return [i for i in range(4, 7) if n % i == 0]