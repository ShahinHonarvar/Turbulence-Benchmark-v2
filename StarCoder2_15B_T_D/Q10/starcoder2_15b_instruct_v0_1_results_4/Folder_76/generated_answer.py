def all_odd_ints_exclusive(int_list):
    """
    Returns the list of all odd integers from index 361 to index 643, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [i for i in int_list[361:643] if i % 2 == 1]