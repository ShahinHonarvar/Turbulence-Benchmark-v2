def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 22 to index 24, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(22, 24):
        if nums[i] % 2 == 1:
            result.append(nums[i])
    return result