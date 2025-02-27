def sum_odd_ints_inclusive(ints):
    """
    Returns the sum of all odd integers from index 50 to index 54, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((i for i in ints[50:55] if i % 2 == 1))