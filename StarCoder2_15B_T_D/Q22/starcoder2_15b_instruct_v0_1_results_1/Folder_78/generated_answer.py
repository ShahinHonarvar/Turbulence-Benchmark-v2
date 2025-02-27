def find_sum_of_multiples(n):
    """
    This function takes a positive integer 'n' as input and returns the sum of the first 48 positive multiples of 'n'.
    """
    sum = 0
    for i in range(1, 49):
        sum += n * i
    return sum