def all_ints_not_div_by_num(nums, num):
    """
    Returns a list of all integers not divisible by 'num' from index 32 to index 44, both exclusive.
    If no such integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in range(32, 44):
        if nums[i] % num != 0:
            result.append(nums[i])
    return result