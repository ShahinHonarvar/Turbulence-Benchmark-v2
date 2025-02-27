def all_pos_ints_inclusive(lst: list) -> list:
    """
    Returns the list of all positive integers from index 35 to index 49, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [num for num in lst[35:50] if num > 0]