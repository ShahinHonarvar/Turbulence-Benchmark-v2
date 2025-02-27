def all_pos_ints_inclusive(nums):
    """
    Returns the list of all positive integers from index 0 to index 7, both inclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    pos_ints = []
    for i in range(8):
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints