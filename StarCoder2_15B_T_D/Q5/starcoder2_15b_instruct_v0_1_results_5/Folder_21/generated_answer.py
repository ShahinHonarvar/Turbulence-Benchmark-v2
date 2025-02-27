def all_neg_ints_inclusive(nums):
    """Returns the list of all negative integers from index 639 to index 975, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned."""
    result = []
    for i in range(639, 976):
        if nums[i] < 0:
            result.append(nums[i])
    return result