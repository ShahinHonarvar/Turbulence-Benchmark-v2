def all_pos_ints_exclusive(nums):
    """
    Returns the list of all positive integers from index 0 to index 3, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = []
    for num in nums:
        if num > 0:
            result.append(num)
    return result[:3]