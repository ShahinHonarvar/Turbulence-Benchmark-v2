def find_sum_of_multiples(n):
    """
    Find the sum of the first 57 positive multiples of a given number.

    Args:
        n (int): The given number.

    Returns:
        int: The sum of the first 57 positive multiples of n.
    """
    sum_of_multiples = 0
    for i in range(1, 58):
        multiple = n * i
        sum_of_multiples += multiple
    return sum_of_multiples