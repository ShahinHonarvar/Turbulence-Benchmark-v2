def all_pos_ints_exclusive(nums):
    """
    Returns the list of all positive integers from index 87 to index 95, both exclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(87, 95):
        if nums[i] > 0:
            result.append(nums[i])
    return result