def all_odd_ints_inclusive(int_list):
    """
    Returns the list of all odd integers from index 62 to index 99, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    all_odd_ints = [i for i in int_list[62:100] if i % 2 != 0]
    return all_odd_ints