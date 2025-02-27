def all_pos_ints_exclusive(nums):
    """
    Returns the list of all positive integers from index 0 to index 6, both exclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    result = []
    for num in nums[0:6]:
        if num > 0:
            result.append(num)
    return result