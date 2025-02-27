def all_even_ints_exclusive(nums):
    """
    Returns the list of all even integers from index 2 to index 7 (exclusive),
    or an empty list if no even integers exist in the specified range.
    """
    result = []
    for i in range(2, 7):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result