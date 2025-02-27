def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 686 to index 987, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 686 and i <= 987 and (num % 2 == 1)]