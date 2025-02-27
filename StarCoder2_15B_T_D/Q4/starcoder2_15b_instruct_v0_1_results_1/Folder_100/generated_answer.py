def all_pos_ints_exclusive(nums):
    """
    Returns the list of all positive integers from index 22 to index 24, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [num for num in nums[22:24] if num > 0]