def all_even_ints_exclusive(nums):
    """
    Returns the list of all even integers from index 0 to index 10, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [num for num in nums[0:10] if num % 2 == 0]