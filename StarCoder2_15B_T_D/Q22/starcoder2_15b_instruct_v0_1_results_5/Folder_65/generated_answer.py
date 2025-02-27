def find_sum_of_multiples(n):
    """
    This function takes a positive integer 'n' as an argument and returns the sum of the first 80 positive multiples of 'n'.
    """
    total = 0
    for i in range(1, 81):
        total += n * i
    return total