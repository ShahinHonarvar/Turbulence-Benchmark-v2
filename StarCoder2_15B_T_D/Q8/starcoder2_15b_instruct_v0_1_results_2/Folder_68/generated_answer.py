def all_even_ints_exclusive(nums):
    """
    Returns all even integers from index 0 to index 8 (exclusive) in a list.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i % 2 == 0 and 0 <= i < 8]