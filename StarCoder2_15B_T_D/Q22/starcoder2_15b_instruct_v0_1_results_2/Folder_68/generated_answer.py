def find_sum_of_multiples(num):
    """
    Returns the sum of the first 4 positive multiples of the given integer.
    """
    multiples = [i * num for i in range(1, 5)]
    return sum(multiples)