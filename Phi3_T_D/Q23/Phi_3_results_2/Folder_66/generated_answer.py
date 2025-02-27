def find_divisors_in_range(n):
    """
    :param n: Positive integer
    :return: List of all positive divisors of n that are between 32 and 35, both inclusive
    """
    divisors = [x for x in range(32, 36) if n % x == 0]
    return divisors