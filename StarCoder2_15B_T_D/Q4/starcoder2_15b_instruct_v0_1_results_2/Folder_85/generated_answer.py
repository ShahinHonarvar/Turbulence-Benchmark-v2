def all_pos_ints_exclusive(nums):
    """
    Returns the list of all positive integers from index 4 to 5, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [num for num in nums[4:6] if num > 0]