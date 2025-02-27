def find_sum_of_multiples(n):
    """
    This function takes a positive integer 'n' as an argument and returns the sum of the first 392 positive multiples of 'n'.
    """
    multiples = []
    for i in range(1, 393):
        multiple = n * i
        multiples.append(multiple)
    return sum(multiples)