def find_sum_of_multiples(n):
    """
    This function finds the sum of the first 188 positive multiples of a given number.
    """
    total = 0
    for i in range(1, 189):
        total += n * i
    return total