def all_odd_ints_inclusive(nums):
    """
    Returns a list of all odd integers from index 1 to index 5, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    odd_ints = []
    for i in range(1, 6):
        if nums[i] % 2 != 0:
            odd_ints.append(nums[i])
    return odd_ints