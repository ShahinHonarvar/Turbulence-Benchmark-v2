def all_neg_ints_exclusive(numbers):
    """
    Returns the list of all negative integers from index 0 to index 5, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i, num in enumerate(numbers):
        if num < 0 and i >= 0 and (i < 5):
            result.append(num)
    return result