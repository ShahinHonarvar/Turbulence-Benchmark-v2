def all_neg_ints_exclusive(integers_list):
    """
    Returns a list of all negative integers from index 323 to 972, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(323, 972):
        if integers_list[i] < 0:
            result.append(integers_list[i])
    return result