def find_sum_of_multiples(num):
    """
    Returns the sum of the first 13 positive multiples of `num`.
    """
    return sum((num * i for i in range(1, 14)))