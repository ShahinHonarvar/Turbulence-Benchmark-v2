def find_sum_of_multiples(n):
    """
    Returns the sum of the first 84 positive multiples of `n`.
    """
    total = 0
    for i in range(1, 85):
        total += n * i
    return total