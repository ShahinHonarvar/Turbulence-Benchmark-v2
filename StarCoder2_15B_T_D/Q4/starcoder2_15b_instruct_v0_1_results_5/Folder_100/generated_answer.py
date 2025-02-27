def all_pos_ints_exclusive(nums):
    """
    Returns the list of all positive integers from index 22 to index 24, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    pos_ints = []
    for i, num in enumerate(nums):
        if 22 <= i < 25 and num > 0:
            pos_ints.append(num)
    return pos_ints