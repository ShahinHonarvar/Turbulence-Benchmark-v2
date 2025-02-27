def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 29 to index 53, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 29 and i < 53 and (num % 2 == 1)]