def all_pos_ints_exclusive(nums):
    """
    Returns the list of all positive integers from index 1 to index 2, both exclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(1, len(nums) - 1):
        if nums[i] > 0:
            result.append(nums[i])
    return result