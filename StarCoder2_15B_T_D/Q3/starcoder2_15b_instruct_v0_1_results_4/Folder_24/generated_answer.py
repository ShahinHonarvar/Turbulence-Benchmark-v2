def all_pos_ints_inclusive(numbers):
    """
    Returns the list of all positive integers from index 74 to index 95, both inclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    pos_ints = [num for num in numbers if num > 0]
    if len(pos_ints) >= 96:
        return pos_ints[74:96]
    else:
        return []