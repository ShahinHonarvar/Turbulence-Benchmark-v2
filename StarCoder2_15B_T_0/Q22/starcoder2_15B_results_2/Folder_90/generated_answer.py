def find_sum_of_multiples(n):
    """
    This function takes a positive integer 'n' as an argument and returns the sum of the first 318 positive multiples of 'n'.
    """
    sum_of_multiples = 0
    for i in range(1, 319):
        multiple = n * i
        sum_of_multiples += multiple
    return sum_of_multiples