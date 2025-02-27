def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers in `nums` from index 0 to index 7, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(nums):
        if i <= 7 and num < 0:
            result.append(num)
    return result