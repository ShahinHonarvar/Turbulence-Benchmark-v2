def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 11 to index 76, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if 11 < i < 76 and num % 2 == 1]