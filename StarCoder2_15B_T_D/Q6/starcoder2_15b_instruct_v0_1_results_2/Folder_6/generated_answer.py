def all_neg_ints_exclusive(nums):
    """Returns the list of all negative integers from index 86 to index 99, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned."""
    neg_ints = []
    for i in range(86, 99):
        if nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints