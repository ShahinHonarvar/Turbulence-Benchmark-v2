def find_sum_of_multiples(n):
    """
    Find the sum of the first 223 positive multiples of n.
    """
    multiples = [i * n for i in range(1, 224)]
    return sum(multiples)