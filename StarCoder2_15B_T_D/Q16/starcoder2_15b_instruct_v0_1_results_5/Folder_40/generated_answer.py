def sum_even_ints_inclusive(ints):
    """
    Returns the sum of all even integers from index 0 to index 2, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    return sum((int for int in ints[0:3] if int % 2 == 0))