def all_odd_ints_exclusive(input_list):
    """
    Returns the list of all odd integers from index 100 to index 101, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(input_list) if i >= 100 and i < 102 and (num % 2 == 1)]