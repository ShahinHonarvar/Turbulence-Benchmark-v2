def all_pos_ints_exclusive(nums):
    """
    Returns the list of all positive integers from index 78 to index 93, both exclusive. If no positive integers exist in the specified range, returns an empty list.
    """
    return [num for num in nums[78:93] if num > 0]