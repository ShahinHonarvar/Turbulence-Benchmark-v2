def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 1 to index 2, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    neg_ints = []
    for i in range(1, 2):
        if nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints