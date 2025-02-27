def find_sum_of_multiples(n):
    """
    Returns the sum of the first 85 positive multiples of `n`.
    """
    multiples_sum = 0
    for i in range(1, 86):
        multiple = n * i
        multiples_sum += multiple
    return multiples_sum