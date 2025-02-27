def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 25 to index 59, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    res = []
    for i in range(25, 60):
        if nums[i] < 0:
            res.append(nums[i])
    return res