def find_sum_of_multiples(num):
    """
    This function takes a positive integer as an argument and returns the sum of the first 51 positive multiples of the given integer.
    """
    sum_of_multiples = 0
    for i in range(1, 52):
        multiple = num * i
        sum_of_multiples += multiple
    return sum_of_multiples