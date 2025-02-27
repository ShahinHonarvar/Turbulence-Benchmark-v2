def find_sum_of_multiples(n):
    """
    This function finds the sum of the first 13 positive multiples of a given integer.
    """
    multiples = [i * n for i in range(1, 14)]
    return sum(multiples)