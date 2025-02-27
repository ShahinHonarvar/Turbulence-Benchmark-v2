def find_sum_of_multiples(n):
    """
    This function takes a positive integer as an argument and returns the sum of the first 338 positive multiples of the given integer.
    """
    multiples = []
    for i in range(1, 339):
        multiple = n * i
        multiples.append(multiple)
    return sum(multiples)