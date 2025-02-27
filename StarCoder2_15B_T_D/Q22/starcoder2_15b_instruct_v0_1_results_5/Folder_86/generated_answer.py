def find_sum_of_multiples(n):
    """
    This function finds the sum of the first 181 positive multiples of a given number.
    """
    multiples = []
    for i in range(1, 182):
        multiple = n * i
        multiples.append(multiple)
    return sum(multiples)