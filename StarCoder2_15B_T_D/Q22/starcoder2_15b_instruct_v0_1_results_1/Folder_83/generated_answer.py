def find_sum_of_multiples(n):
    """
    This function takes a positive integer as an argument and returns the sum of the first 73 positive multiples of the integer.
    """
    return sum((n * i for i in range(1, 74)))