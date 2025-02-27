def all_odd_ints_inclusive(ints_list):
    """
    Returns the list of all odd integers from index 22 to index 88, both inclusive.
    If no odd integers exist in the specified range, the function returns an empty list.
    """
    return [x for i, x in enumerate(ints_list) if i >= 22 and i <= 88 and (x % 2 != 0)]