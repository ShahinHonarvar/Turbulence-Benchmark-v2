def all_neg_ints_inclusive(nums):
    """Return the list of all negative integers from index 0 to index 3, both inclusive.
    If no negative integers exist in the specified range, return an empty list."""
    return [num for num in nums[:4] if num < 0]