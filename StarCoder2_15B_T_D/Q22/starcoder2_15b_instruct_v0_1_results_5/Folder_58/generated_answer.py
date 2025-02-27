def find_sum_of_multiples(n):
    """
    This function takes a positive integer and returns the sum of the first 223 positive multiples of the given integer.
    """
    sum_of_multiples = 0
    for i in range(1, 224):
        multiple = n * i
        sum_of_multiples += multiple
    return sum_of_multiples