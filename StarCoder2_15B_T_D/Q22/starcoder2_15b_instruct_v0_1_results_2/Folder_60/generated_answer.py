def find_sum_of_multiples(num):
    """
    Returns the sum of the first 35 positive multiples of the given number.
    """
    return sum(range(num, num * 36, num))