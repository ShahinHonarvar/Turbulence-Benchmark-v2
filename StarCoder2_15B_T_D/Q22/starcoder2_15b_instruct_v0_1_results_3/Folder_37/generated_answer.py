def find_sum_of_multiples(n):
    """
    Returns the sum of the first 17 positive multiples of n.
    """
    multiples = []
    for i in range(1, 18):
        multiples.append(n * i)
    return sum(multiples)