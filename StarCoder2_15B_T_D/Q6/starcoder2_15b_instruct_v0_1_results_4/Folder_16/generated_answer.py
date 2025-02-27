def all_neg_ints_exclusive(numbers):
    """
    Returns the list of all negative integers from index 86 to index 90, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i, num in enumerate(numbers):
        if num < 0 and 86 <= i < 90:
            result.append(num)
    return result