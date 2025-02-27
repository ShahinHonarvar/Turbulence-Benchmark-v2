def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 66 to index 90, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if 66 < i < 90 and num < 0]