def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 62 to index 99, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 62 and i <= 99 and (num % 2 == 0)]