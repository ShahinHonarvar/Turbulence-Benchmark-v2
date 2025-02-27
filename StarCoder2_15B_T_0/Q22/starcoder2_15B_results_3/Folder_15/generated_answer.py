def find_sum_of_multiples(num):
    """
    Returns the sum of the first 3 positive multiples of the given number.
    """
    multiples = []
    for i in range(1, 4):
        multiple = num * i
        multiples.append(multiple)
    return sum(multiples)