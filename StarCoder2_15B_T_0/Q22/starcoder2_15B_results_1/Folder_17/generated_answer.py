def find_sum_of_multiples(n):
    """
    This function takes a positive integer 'n' as an argument and returns the sum of the first 289 positive multiples of 'n'.
    """
    multiples = [i * n for i in range(1, 290)]
    return sum(multiples)