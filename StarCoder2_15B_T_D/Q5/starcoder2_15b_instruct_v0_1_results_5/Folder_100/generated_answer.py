def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 42 to index 68, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [num for num in nums[42:70] if num < 0]