def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 0 to index 2, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [num for num in nums if num < 0 and 0 <= nums.index(num) <= 2]