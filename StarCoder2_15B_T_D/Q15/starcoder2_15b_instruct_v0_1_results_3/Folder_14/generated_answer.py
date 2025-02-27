def sum_odd_ints_inclusive(ints):
    """
    Returns the sum of all odd integers from index 5 to index 7, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((x for x in ints[5:8] if x % 2 != 0))