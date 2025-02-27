def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers from index 56 to index 92, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [i for i in ints[56:92] if i % 2 == 1]