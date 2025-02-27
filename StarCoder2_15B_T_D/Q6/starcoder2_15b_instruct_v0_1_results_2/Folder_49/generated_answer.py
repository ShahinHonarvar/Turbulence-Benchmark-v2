def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 80 to index 200, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(80, 200):
        if nums[i] < 0:
            result.append(nums[i])
    return result