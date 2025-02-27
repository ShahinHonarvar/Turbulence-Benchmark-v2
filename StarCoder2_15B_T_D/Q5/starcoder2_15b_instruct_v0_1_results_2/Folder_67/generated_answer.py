from the given list of integers. If no negative integers exist in the specified range,

def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 22 to index 50, both inclusive,
    an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 22 and i <= 50 and (num < 0)]