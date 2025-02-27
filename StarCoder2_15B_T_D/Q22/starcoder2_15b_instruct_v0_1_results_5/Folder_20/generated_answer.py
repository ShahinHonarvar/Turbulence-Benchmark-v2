def find_sum_of_multiples(n):
    """
    Find the sum of the first 45 positive multiples of a given integer.
    """
    total = 0
    for i in range(1, 46):
        multiple = n * i
        total += multiple
    return total