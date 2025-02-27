def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 1 to index 7, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i % 2 == 1 and 1 <= i < 7]