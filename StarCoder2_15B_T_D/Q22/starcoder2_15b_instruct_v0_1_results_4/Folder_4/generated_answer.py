def find_sum_of_multiples(num):
    """
    This function takes a positive integer and returns the sum of the first 40 positive multiples of the integer.
    """
    return sum((num * i for i in range(1, 41)))