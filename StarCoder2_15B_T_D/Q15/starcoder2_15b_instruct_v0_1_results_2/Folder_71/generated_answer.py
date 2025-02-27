def sum_odd_ints_inclusive(list_of_ints):
    """
    Returns the sum of all odd integers from index 26 to index 52, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((i for i in list_of_ints[26:53] if i % 2 != 0))