def find_sum_of_multiples(n):
    """
    Find the sum of the first 19 positive multiples of n.
    """
    result = 0
    for i in range(1, 20):
        result += n * i
    return result