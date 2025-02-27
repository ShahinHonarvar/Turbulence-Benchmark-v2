def find_sum_of_multiples(num):
    """
    This function returns the sum of the first 17 positive multiples of the given number.
    """
    multiples = [i * num for i in range(1, 18)]
    return sum(multiples)