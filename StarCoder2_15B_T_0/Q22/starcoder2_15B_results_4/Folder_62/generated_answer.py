def find_sum_of_multiples(n):
    """
    Returns the sum of the first 188 positive multiples of n.
    """
    multiples = [i * n for i in range(1, 189)]
    return sum(multiples)