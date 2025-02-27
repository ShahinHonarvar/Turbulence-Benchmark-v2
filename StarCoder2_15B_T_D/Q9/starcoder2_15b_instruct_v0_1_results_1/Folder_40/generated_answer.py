def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 0 to index 2, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    odd_ints = []
    for i in range(len(nums)):
        if i >= 0 and i <= 2 and (nums[i] % 2 != 0):
            odd_ints.append(nums[i])
    return odd_ints