def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 57 to index 84, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for num in nums[57:84]:
        if num < 0:
            result.append(num)
    return result