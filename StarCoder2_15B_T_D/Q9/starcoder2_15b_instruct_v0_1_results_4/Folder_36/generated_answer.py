def all_odd_ints_inclusive(my_list):
    """
    Returns the list of all odd integers from index 246 to index 750, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    start_index = 246
    end_index = 750
    return [num for i, num in enumerate(my_list) if i >= start_index and i <= end_index and (num % 2 != 0)]