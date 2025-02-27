def all_odd_ints_inclusive(ints):
    """
    Returns a list of all the odd integers from index 55 to index 98, both inclusive.
    If no odd integers exist in the specified range, return an empty list.
    """
    return [i for i in ints[55:99] if i % 2 != 0]