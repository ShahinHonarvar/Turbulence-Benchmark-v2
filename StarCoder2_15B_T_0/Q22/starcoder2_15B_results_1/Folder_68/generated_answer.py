def find_sum_of_multiples(num):
    """
    Returns the sum of the first 4 positive multiples of the given number.
    """
    multiples = []
    for i in range(1, 10):
        if num * i > 0:
            multiples.append(num * i)
        if len(multiples) == 4:
            break
    return sum(multiples)