def find_sum_of_multiples(num):
    """
    This function takes a positive integer as an argument and returns the sum of the first 54 positive multiples of the given integer.
    """
    multiples = [i * num for i in range(1, 55)]
    return sum(multiples)