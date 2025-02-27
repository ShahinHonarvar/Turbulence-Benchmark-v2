def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 0 to index 2, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for num in nums if num % 2 != 0 and 0 <= num <= 2]