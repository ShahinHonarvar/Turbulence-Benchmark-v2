def all_odd_ints_inclusive(lst):
    """
    Returns the list of all odd integers from index 20 to index 30, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [x for i, x in enumerate(lst) if i >= 20 and i <= 30 and (x % 2 == 1)]