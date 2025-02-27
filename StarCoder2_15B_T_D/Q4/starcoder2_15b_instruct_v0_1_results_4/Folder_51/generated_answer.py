def all_pos_ints_exclusive(nums):
    """
    Returns the list of all positive integers from index 6 to index 9, both exclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    pos_ints = [num for num in nums[6:9] if num > 0]
    return pos_ints