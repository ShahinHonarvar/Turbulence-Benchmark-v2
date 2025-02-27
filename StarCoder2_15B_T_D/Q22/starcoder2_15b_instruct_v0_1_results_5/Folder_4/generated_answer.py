def find_sum_of_multiples(num):
    """
    Find the sum of the first 40 positive multiples of a given number.
    """
    multiples = []
    for i in range(1, 41):
        multiple = num * i
        multiples.append(multiple)
    return sum(multiples)