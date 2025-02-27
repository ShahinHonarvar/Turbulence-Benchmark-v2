def all_odd_ints_exclusive(my_list):
    """
    Returns the list of all odd integers from index 1 to index 2, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(my_list) if i % 2 == 1 and 1 <= i < len(my_list) - 1]