def all_pos_ints_inclusive(nums):
    """
    Returns the list of all positive integers from index 23 to index 23, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = []
    for num in nums:
        if num > 0:
            result.append(num)
    return result[23:24]