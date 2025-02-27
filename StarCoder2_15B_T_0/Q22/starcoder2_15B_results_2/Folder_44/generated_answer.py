def find_sum_of_multiples(n):
    """
    Find the sum of the first 445 positive multiples of a given integer.
    """
    multiples = []
    for i in range(1, 446):
        multiple = n * i
        multiples.append(multiple)
    return sum(multiples)