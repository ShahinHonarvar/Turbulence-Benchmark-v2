def all_odd_ints_exclusive(int_list):
    """
    Returns the list of all odd integers from index 20 to index 200, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [i for i in int_list[20:200] if i % 2 != 0]