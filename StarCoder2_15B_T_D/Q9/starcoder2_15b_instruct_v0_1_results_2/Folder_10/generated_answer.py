def all_odd_ints_inclusive(int_list):
    """Returns the list of all odd integers from index 25 to index 59, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned."""
    return [x for i, x in enumerate(int_list) if i >= 25 and i <= 59 and (x % 2 != 0)]