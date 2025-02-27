def find_sum_of_multiples(num):
    """
    This function finds the sum of the first 475 positive multiples of a given number.
    """
    multiples = [i * num for i in range(1, 476)]
    return sum(multiples)