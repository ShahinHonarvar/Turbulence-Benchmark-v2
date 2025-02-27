def all_neg_ints_inclusive(nums):
    """
    Returns all negative integers from index 14 to index 64, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 14 and i <= 64 and (num < 0)]