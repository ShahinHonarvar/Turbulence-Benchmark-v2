def find_sum_of_multiples(number):
    """
    Returns the sum of the first 28 positive multiples of the given number.
    """
    multiples = [i * number for i in range(1, 29)]
    return sum(multiples)