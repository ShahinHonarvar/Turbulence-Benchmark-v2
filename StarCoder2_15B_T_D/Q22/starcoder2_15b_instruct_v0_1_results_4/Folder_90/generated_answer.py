def find_sum_of_multiples(n):
    """
    Returns the sum of the first 318 positive multiples of `n`.
    """
    sum = 0
    for i in range(1, 319):
        multiple = n * i
        sum += multiple
    return sum