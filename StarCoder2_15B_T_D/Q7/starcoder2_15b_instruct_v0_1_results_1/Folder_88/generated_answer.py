def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 4 to index 8, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i >= 4 and i <= 8 and (num % 2 == 0)]