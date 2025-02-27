def find_sum_of_multiples(n):
    """
    Find the sum of the first 66 positive multiples of a given integer.
    Args:
        n (int): The given integer.
    Returns:
        int: The sum of the first 66 positive multiples of `n`.
    """
    multiples = [i * n for i in range(1, 67)]
    return sum(multiples)