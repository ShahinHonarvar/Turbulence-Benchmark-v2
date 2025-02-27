def find_sum_of_multiples(n):
    """
    Returns the sum of the first 99 positive multiples of n.
    """
    multiples = [i * n for i in range(1, 100)]
    return sum(multiples)