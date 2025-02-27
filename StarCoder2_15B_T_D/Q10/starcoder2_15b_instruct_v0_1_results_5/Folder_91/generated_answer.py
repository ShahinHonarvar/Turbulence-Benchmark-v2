def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 0 to index 5, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for num in nums[0:5] if num % 2 == 1]