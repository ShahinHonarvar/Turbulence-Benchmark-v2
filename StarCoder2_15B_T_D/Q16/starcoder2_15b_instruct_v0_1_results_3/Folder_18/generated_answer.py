def sum_even_ints_inclusive(ints):
    """
    Returns the sum of all even integers from index 35 to index 49, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    return sum((x for x in ints[35:50] if x % 2 == 0))