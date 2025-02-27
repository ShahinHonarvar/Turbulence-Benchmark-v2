def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 20 to index 36, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 20 and i < 36 and (num % 2 == 1)]