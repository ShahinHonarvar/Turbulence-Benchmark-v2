def all_odd_ints_exclusive(int_list):
    """
    Returns the list of all odd integers from index 25 to index 80, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for idx, num in enumerate(int_list) if idx >= 25 and idx < 80 and (num % 2 == 1)]