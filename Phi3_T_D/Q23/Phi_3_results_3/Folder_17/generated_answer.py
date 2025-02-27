def find_divisors_in_range(n):
    """
    Find all positive divisors of n that are between 10 and 69 inclusive.

    Args:
    n (int): The positive integer to find divisors of.

    Returns:
    list: A list of divisors of n in the range 10-69.
    """
    divisors = [divisor for divisor in range(10, 70) if n % divisor == 0]
    return divisors