def find_sum_of_multiples(num):
    """
    This function takes a positive integer as input and returns the sum of the first 147
    positive multiples of the given integer.
    """
    return sum((num * i for i in range(1, 148)))