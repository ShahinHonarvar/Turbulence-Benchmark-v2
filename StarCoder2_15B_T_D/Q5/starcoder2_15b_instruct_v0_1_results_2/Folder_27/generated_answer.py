def all_neg_ints_inclusive(nums):
    """
    Function to return all negative integers from index 66 to index 93, both inclusive.
    If no negative integers exist in the specified range, the function should return an empty list.
    """
    if any((num < 0 for num in nums)):
        return [num for num in nums[66:94] if num < 0]
    else:
        return []