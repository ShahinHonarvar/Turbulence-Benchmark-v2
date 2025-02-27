def all_odd_ints_inclusive(lst):
    """
    Returns the list of all odd integers from index 68 to index 86, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[68:87] if x % 2 != 0]