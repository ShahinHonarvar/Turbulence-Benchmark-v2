def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 43 to index 51, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 43 and i <= 51 and (num % 2 == 1)]