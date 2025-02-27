def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 0 to index 0, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    if not nums:
        return []
    result = []
    for num in nums:
        if num < 0:
            result.append(num)
    return result