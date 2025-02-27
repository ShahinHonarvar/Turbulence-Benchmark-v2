def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 0 to index 5, both exclusive.
    If no negative integers exist in the specified range, return an empty list.
    """
    result = []
    for num in nums[:5]:
        if num < 0:
            result.append(num)
    return result