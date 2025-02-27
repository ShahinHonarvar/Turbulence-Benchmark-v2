def find_sum_of_multiples(n):
    """
    This function takes a positive integer 'n' and returns the sum of the first 276 positive multiples of 'n'.
    """
    multiples_sum = 0
    for i in range(1, 277):
        multiple = n * i
        multiples_sum += multiple
    return multiples_sum