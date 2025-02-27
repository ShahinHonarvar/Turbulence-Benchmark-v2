def all_pos_ints_inclusive(nums):
    """
    Returns the list of all positive integers from index 8 to index 9, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [num for num in nums[8:10] if num > 0]