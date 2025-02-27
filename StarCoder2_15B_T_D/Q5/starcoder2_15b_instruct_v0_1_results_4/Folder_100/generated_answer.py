def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 42 to index 68, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [num for num in nums[42:69] if num < 0]