def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 1 to index 8, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in range(1, 9):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result