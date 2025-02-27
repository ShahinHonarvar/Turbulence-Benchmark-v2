def sum_odd_ints_inclusive(ints):
    """
    Returns the sum of all odd integers from index 22 to index 63, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((i for i in ints[22:64] if i % 2 != 0))