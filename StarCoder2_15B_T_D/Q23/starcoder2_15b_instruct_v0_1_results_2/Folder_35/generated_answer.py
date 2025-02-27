def find_divisors_in_range(n):
    """
    Finds the list of all positive divisors of the given integer that are between 392 and 465, both inclusive.
    If no such divisors exist in the specified range, returns an empty list.
    """
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and 392 <= i <= 465:
            divisors.append(i)
    return divisors