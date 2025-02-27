def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 246 to index 750, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 246 and i <= 750 and (num % 2 == 0)]