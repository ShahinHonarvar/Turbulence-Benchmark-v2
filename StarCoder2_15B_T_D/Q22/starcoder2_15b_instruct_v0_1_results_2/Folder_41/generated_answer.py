def find_sum_of_multiples(number):
    """
    This function takes a positive integer and returns the sum of the first 63 positive multiples of the given integer.
    """
    multiples = [i * number for i in range(1, 64)]
    return sum(multiples)