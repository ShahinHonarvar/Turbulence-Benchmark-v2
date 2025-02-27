def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 50 to index 54, both inclusive,
    in the input list. If no positive integers exist in the specified range, an empty list
    is returned.
    """
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 50 <= i <= 54:
            result.append(num)
    return result