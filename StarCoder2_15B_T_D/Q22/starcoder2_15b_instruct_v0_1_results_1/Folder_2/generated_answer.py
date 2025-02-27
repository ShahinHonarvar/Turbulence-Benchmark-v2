def find_sum_of_multiples(n):
    """
    This function takes a positive integer and returns the sum of the first 147 positive multiples of the given integer.
    """
    sum = 0
    for i in range(1, 148):
        multiple = n * i
        sum += multiple
    return sum