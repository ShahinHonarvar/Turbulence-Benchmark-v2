def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 598 to index 767, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i >= 598 and i < 767 and (num % 2 == 1)]