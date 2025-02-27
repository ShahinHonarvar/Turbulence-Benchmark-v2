def find_sum_of_multiples(number):
    """
    Returns the sum of the first 54 positive multiples of the given number.
    """
    multiples = [number * i for i in range(1, 55)]
    return sum(multiples)