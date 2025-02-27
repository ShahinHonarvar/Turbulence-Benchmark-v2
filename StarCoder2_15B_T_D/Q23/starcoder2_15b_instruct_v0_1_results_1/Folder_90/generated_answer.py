def find_divisors_in_range(num: int) -> list:
    """
    Finds all positive divisors of the given integer that are between 451 and 973, both inclusive.
    If no such divisors exist, returns an empty list.
    """
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0 and 451 <= i <= 973:
            divisors.append(i)
    return divisors