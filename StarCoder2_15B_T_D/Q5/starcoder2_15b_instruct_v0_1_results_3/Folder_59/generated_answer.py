def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 0 to index 9, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(lst):
        if num < 0 and i >= 0 and (i <= 9):
            result.append(num)
    return result