def find_sum_of_multiples(num):
    """
    This function finds the sum of the first 68 positive multiples of a given number.
    """
    sum_of_multiples = 0
    for i in range(1, 69):
        multiple = num * i
        sum_of_multiples += multiple
    return sum_of_multiples