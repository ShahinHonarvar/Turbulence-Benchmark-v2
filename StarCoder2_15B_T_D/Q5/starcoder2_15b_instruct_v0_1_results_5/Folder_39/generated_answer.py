def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 20 to index 30, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(20, 31):
        if nums[i] < 0:
            result.append(nums[i])
    return result