def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers from index 10 to index 79, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [i for i in ints[10:80] if i % 2 == 1]