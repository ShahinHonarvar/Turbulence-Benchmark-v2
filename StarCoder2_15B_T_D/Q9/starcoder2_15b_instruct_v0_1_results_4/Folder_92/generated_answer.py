def all_odd_ints_inclusive(nums):
    """
    Returns a list of all odd integers from index 0 to index 1, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(len(nums)):
        if i % 2 == 1:
            result.append(nums[i])
    return result