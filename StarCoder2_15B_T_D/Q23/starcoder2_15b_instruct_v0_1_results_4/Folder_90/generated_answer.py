def find_divisors_in_range(n):
    """
    Returns the list of all positive divisors of the given integer n that are between 451 and 973, both inclusive.
    If no such divisors exist, returns an empty list.
    """
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and 451 <= i <= 973:
            divisors.append(i)
    return divisors