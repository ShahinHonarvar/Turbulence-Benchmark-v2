def find_sum_of_multiples(num):
    """
    Returns the sum of the first 188 positive multiples of the given number.
    """
    multiples_sum = 0
    for i in range(1, 189):
        multiple = num * i
        multiples_sum += multiple
    return multiples_sum