def all_neg_ints_inclusive(nums):
    """
    Returns a list of all negative integers from index 0 to index 2, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [num for num in nums[0:3] if num < 0]