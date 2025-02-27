def find_sum_of_multiples(num):
    """Find the sum of the first 445 positive multiples of a given integer."""
    multiples = [i * num for i in range(1, 446)]
    return sum(multiples)