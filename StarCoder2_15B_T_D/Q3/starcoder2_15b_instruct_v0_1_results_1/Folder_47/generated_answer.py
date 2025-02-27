def all_pos_ints_inclusive(nums):
    """
    Returns the list of all positive integers from index 37 to index 76, both inclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    pos_ints = []
    for i in range(37, 77):
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints