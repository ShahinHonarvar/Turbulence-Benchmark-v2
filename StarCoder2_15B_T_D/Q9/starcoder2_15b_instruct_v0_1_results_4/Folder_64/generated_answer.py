def all_odd_ints_inclusive(my_list):
    """
    Returns the list of all odd integers from index 0 to index 4, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [i for i in my_list[0:5] if i % 2 != 0]