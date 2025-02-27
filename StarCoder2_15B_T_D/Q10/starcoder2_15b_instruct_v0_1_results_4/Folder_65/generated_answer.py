def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 42 to index 87, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i >= 42 and i < 87 and (num % 2 == 1)]