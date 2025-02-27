def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 1 to index 8, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i >= 1 and i <= 8 and (num < 0)]