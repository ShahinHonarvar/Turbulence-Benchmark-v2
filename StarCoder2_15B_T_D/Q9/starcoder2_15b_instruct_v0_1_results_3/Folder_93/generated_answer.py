def all_odd_ints_inclusive(ints):
    """
    Returns all odd integers from index 75 to index 94, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [i for i in ints[75:95] if i % 2 == 1]