def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 22 to index 88, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i >= 22 and i <= 88 and (num % 2 == 1)]