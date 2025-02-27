def find_sum_of_multiples(n):
    """
    Find the sum of the first 206 positive multiples of the given integer.
    """
    total = 0
    for i in range(1, 207):
        multiple = n * i
        total += multiple
    return total