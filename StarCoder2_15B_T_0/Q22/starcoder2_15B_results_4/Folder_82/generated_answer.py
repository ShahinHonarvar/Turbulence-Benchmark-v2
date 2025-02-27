def find_sum_of_multiples(num):
    """
    Returns the sum of the first 33 positive multiples of the given number.
    """
    multiples = [i * num for i in range(1, 34)]
    return sum(multiples)