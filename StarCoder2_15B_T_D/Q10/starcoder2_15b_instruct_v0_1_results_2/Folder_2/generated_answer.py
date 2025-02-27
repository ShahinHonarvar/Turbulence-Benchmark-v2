def all_odd_ints_exclusive(lst):
    """Returns the list of all odd integers from index 36 to index 52, both exclusive.
    If no odd integers exist in the specified range, the function should return an empty list.
    """
    return [x for i, x in enumerate(lst) if 36 < i < 52 and x % 2 != 0]