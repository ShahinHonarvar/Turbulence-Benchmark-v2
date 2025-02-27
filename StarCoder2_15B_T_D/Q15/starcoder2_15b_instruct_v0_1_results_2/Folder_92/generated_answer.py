def sum_odd_ints_inclusive(ints):
    """
    Returns the sum of all odd integers in the list 'ints' from index 1 to index 1 (inclusive).
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((i for i in ints[1:2] if i % 2 != 0))