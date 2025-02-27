def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 4 to 5, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    odd_ints = []
    for i in range(4, 5):
        if nums[i] % 2 == 1:
            odd_ints.append(nums[i])
    return odd_ints