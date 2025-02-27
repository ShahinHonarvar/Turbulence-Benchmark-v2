def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 6 to index 9, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(nums):
        if num < 0 and 6 <= i < 9:
            result.append(num)
    return result