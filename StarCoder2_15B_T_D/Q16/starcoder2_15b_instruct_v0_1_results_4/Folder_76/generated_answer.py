def sum_even_ints_inclusive(ints):
    """
    Returns the sum of all even integers from index 686 to index 987, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    return sum((int for int in ints[686:988] if int % 2 == 0))