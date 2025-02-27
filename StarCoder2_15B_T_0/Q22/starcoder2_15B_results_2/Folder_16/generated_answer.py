def find_sum_of_multiples(n):
    """
    Returns the sum of the first 255 positive multiples of n.
    """
    sum_of_multiples = 0
    for i in range(1, 256):
        multiple = n * i
        sum_of_multiples += multiple
    return sum_of_multiples