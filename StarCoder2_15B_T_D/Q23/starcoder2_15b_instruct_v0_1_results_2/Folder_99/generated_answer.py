def find_divisors_in_range(num):
    """
    Finds the list of all positive divisors of a given integer that are between 378 and 782, both inclusive.
    If no such divisors exist in the specified range, an empty list is returned.

    Args:
        num (int): The integer to find divisors for.

    Returns:
        list[int]: A list of all positive divisors of `num` that are between 378 and 782, both inclusive. If no such divisors exist, an empty list is returned.
    """
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    if not divisors:
        return []
    return [divisor for divisor in divisors if 378 <= divisor <= 782]