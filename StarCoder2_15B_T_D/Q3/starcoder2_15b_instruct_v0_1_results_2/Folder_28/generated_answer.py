def all_pos_ints_inclusive(lst):
    """
    Returns a list of all positive integers from index 62 to 63, both inclusive, in the given list.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 62 <= i <= 63:
            result.append(num)
    return result