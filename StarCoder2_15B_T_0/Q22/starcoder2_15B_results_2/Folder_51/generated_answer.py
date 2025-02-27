def find_sum_of_multiples(num):
    """
    This function takes a positive integer as an argument and returns the sum of the first 84 positive multiples of the given integer.
    """
    multiples = []
    for i in range(1, 85):
        multiple = num * i
        multiples.append(multiple)
    return sum(multiples)