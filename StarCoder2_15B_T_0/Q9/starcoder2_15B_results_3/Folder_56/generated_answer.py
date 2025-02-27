def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 0 to index 0, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [num for num in nums if num % 2 == 1]