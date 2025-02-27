def find_sum_of_multiples(n):
    """
    Find the sum of the first 223 positive multiples of a given number.
    """
    sum_of_multiples = 0
    for i in range(1, 224):
        multiple = n * i
        sum_of_multiples += multiple
    return sum_of_multiples