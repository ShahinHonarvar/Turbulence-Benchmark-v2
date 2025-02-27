def find_sum_of_multiples(n):
    """
    Returns the sum of the first 99 positive multiples of a given integer.
    """
    assert isinstance(n, int) and n > 0, "Invalid input: 'n' must be a positive integer."
    total_sum = 0
    for i in range(1, 100):
        total_sum += n * i
    return total_sum