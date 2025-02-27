def all_odd_ints_exclusive(int_list):
    """
    Returns a list of all odd integers from index 0 to index 7, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [i for i in int_list[0:7] if i % 2 == 1]