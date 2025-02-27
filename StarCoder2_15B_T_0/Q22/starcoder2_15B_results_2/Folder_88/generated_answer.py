def find_sum_of_multiples(n):
    """
    Returns the sum of the first 23 positive multiples of n.
    """
    multiples = [i * n for i in range(1, 24)]
    return sum(multiples)