def all_even_ints_exclusive(nums):
    """Returns the list of all even integers from index 100 to index 101, both exclusive.
    If no even integers exist in the specified range, an empty list is returned."""
    return [num for i, num in enumerate(nums) if i >= 100 and i < 102 and (num % 2 == 0)]