def all_pos_ints_inclusive(nums):
    """
    Returns the list of all positive integers from index 60 to index 200, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [num for num in nums[60:201] if num > 0]