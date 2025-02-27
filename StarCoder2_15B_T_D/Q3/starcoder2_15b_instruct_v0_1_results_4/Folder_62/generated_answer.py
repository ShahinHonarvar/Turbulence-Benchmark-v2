def all_pos_ints_inclusive(nums):
    """
    Returns the list of all positive integers from index 91 to index 99, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    pos_ints = []
    for i, num in enumerate(nums):
        if num > 0 and 91 <= i <= 99:
            pos_ints.append(num)
    return pos_ints