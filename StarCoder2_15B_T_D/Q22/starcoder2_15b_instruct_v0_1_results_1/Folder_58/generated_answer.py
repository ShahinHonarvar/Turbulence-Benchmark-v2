def find_sum_of_multiples(n):
    """
    This function takes a positive integer as input and returns the sum of the first 223 positive multiples of the given integer.
    """
    multiples = []
    for i in range(1, 224):
        multiples.append(n * i)
    return sum(multiples)