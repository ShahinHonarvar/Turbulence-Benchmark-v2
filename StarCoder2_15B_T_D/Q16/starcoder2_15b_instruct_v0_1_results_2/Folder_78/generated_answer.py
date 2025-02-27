def sum_even_ints_inclusive(ints):
    """
    Returns the sum of all even integers from index 43 to index 51, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    total = 0
    for i in range(43, 52):
        if ints[i] % 2 == 0:
            total += ints[i]
    return total