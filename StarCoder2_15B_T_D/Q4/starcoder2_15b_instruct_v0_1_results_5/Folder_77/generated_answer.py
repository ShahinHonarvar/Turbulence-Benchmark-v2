def all_pos_ints_exclusive(lst):
    """
    Returns the list of all positive integers from index 111 to index 473, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = []
    for num in lst[111:473]:
        if num > 0:
            result.append(num)
    return result