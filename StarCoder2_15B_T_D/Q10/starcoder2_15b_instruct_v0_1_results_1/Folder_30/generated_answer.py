def all_odd_ints_exclusive(ints):
    """Returns the list of all odd integers from index 86 to index 89, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(ints) if 86 < i < 89 and x % 2 == 1]