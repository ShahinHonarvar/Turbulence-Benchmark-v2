def all_even_ints_inclusive(nums):
    """
    Returns all even integers from index 10 to index 66 (inclusive) in a list of integers.
    If no even integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 10 and i <= 66 and (num % 2 == 0)]