def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 30 to index 48, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(30, 49):
        if nums[i] < 0:
            result.append(nums[i])
    return result