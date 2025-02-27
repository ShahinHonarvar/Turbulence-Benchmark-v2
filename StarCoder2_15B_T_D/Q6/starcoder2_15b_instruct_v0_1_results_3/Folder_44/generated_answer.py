def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 81 to index 86, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [num for num in nums[81:86] if num < 0]