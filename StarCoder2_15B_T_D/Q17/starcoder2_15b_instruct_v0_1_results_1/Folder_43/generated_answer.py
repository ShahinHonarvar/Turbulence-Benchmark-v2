def all_ints_div_by_both_two_nums(nums):
    """
    Returns the list of all integers divisible by both -77 and -32 from index 57 to index 85, both inclusive.
    If no such integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in range(57, 86):
        if nums[i] % -77 == 0 and nums[i] % -32 == 0:
            result.append(nums[i])
    return result