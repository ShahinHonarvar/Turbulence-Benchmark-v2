def find_sum_of_multiples(num):
    """
    Returns the sum of the first 338 positive multiples of num.
    """
    total = 0
    for i in range(1, 339):
        total += num * i
    return total