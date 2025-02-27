def find_sum_of_multiples(num):
    """
    Find the sum of the first 69 positive multiples of a given number.
    """
    multiples = []
    for i in range(1, 70):
        multiple = num * i
        multiples.append(multiple)
    sum_of_multiples = sum(multiples)
    return sum_of_multiples