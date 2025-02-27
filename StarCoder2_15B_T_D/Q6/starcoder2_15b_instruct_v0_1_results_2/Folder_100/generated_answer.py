def all_neg_ints_exclusive(input_list):
    """
    Returns the list of all negative integers from index 22 to index 24, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(input_list):
        if num < 0 and 22 <= i < 24:
            result.append(num)
    return result