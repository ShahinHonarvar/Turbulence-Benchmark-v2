def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 533 to index 605, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 533 and i <= 605 and (num < 0)]