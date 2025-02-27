def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 20 to 36, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i >= 20 and i < 36 and (num < 0)]