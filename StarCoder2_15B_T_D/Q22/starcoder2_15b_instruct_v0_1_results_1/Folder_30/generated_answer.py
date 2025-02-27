def find_sum_of_multiples(n):
    """
    Finds the sum of the first 78 positive multiples of a given integer.
    """
    multiples = [i * n for i in range(1, 79)]
    return sum(multiples)