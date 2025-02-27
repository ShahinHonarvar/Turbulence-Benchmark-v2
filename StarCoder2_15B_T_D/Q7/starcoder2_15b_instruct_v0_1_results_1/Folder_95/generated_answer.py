def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 82 to index 86, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    even_nums = [num for num in nums[82:87] if num % 2 == 0]
    return even_nums