def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 68 to 99, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [num for num in nums if num < 0][68:99]