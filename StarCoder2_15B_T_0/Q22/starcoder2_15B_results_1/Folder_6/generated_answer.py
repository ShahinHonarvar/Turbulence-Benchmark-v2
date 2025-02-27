def find_sum_of_multiples(n):
    """
    Returns the sum of the first 474 positive multiples of n.
    """
    sum = 0
    for i in range(1, 475):
        multiple = n * i
        sum += multiple
    return sum