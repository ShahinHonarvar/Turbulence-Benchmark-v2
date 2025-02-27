def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 56 to index 57, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    odd_ints = []
    for i in range(56, 58):
        if nums[i] % 2 != 0:
            odd_ints.append(nums[i])
    return odd_ints