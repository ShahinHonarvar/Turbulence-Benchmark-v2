def all_neg_ints_exclusive(lst):
    """
    Returns the list of all negative integers from index 10 to index 100, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(lst):
        if num < 0 and 10 <= i < 100:
            result.append(num)
    return result