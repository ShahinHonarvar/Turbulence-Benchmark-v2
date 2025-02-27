def find_sum_of_multiples(num):
    """
    Find the sum of the first 91 positive multiples of a given number.
    """
    return sum((num * i for i in range(1, 92)))