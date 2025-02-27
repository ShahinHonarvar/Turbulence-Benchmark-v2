def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 80 to index 200, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    res = []
    for i, num in enumerate(nums):
        if i >= 80 and i < 200 and (num < 0):
            res.append(num)
    return res