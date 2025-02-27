def sum_odd_ints_inclusive(ints):
    """
    Returns the sum of all odd integers from index 32 to index 35, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((i for i in ints[32:36] if i % 2 == 1))