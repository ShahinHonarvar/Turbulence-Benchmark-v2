def find_sum_of_multiples(n):
    """
    Returns the sum of the first 181 positive multiples of n.
    """
    return sum((n * i for i in range(1, 182)))