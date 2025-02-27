def find_sum_of_multiples(n):
    """
    Find the sum of the first 72 positive multiples of the given integer n.
    """
    multiples = [i * n for i in range(1, 73)]
    return sum(multiples)