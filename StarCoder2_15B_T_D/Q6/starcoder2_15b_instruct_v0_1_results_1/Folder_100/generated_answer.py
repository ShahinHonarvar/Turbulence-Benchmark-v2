def all_neg_ints_exclusive(nums):
    """Returns the list of all negative integers from index 22 to index 24, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i >= 22 and i < 24 and (num < 0)]