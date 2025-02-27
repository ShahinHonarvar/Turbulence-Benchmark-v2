def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 35 to index 49, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [num for num in nums[35:50] if num < 0]