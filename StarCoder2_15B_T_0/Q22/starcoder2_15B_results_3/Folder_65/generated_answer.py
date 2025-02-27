def find_sum_of_multiples(n):
    """
    Returns the sum of the first 80 positive multiples of n.
    """
    multiples = [i * n for i in range(1, 81)]
    return sum(multiples)