def find_sum_of_multiples(n):
    """
    Returns the sum of the first 100 positive multiples of n.
    """
    multiples = [i * n for i in range(1, 101)]
    return sum(multiples)