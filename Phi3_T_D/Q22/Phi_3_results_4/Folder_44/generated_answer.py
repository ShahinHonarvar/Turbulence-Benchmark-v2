def find_sum_of_multiples(n):
    """
    Return the sum of the first 445 positive multiples of the given integer n.
    """
    return sum((n * i for i in range(1, 446)))