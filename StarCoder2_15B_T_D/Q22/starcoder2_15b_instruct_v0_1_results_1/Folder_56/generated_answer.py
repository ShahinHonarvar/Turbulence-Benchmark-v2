def find_sum_of_multiples(num):
    """
    Returns the sum of the first 64 positive multiples of `num`.
    """
    sum_of_multiples = 0
    for i in range(1, 65):
        multiple = num * i
        sum_of_multiples += multiple
    return sum_of_multiples