def find_sum_of_multiples(n):
    """
    Find the sum of the first 464 positive multiples of a given integer.
    """
    sum = 0
    for i in range(1, 465):
        multiple = n * i
        sum += multiple
    return sum