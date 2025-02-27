def find_sum_of_multiples(n):
    """
    This function finds the sum of the first 23 positive multiples of a given
    integer.
    """
    multiples = []
    for i in range(1, 24):
        multiple = n * i
        multiples.append(multiple)
    sum_of_multiples = sum(multiples)
    return sum_of_multiples