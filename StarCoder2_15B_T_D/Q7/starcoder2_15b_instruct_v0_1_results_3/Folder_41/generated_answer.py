def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 6 to index 6, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [num for num in nums[6:7] if num % 2 == 0]