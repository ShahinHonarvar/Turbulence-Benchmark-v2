def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 22 to index 88, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(len(nums)):
        if i >= 22 and i <= 88 and (nums[i] % 2 == 1):
            result.append(nums[i])
    return result