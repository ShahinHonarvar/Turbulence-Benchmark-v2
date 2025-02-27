def find_sum_of_multiples(number):
    """
    Returns the sum of the first 66 positive multiples of the given number.
    """
    sum_of_multiples = 0
    for i in range(1, 67):
        multiple = number * i
        sum_of_multiples += multiple
    return sum_of_multiples