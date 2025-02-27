def all_pos_ints_exclusive(nums):
    """
    Returns a list of all positive integers from index 70 to index 98, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    pos_ints = []
    for i, num in enumerate(nums):
        if num > 0 and 70 < i < 98:
            pos_ints.append(num)
    return pos_ints