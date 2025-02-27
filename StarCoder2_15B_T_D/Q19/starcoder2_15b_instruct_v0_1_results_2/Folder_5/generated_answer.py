def all_ints_not_div_by_num(nums):
    """
    Returns the list of all integers not divisible by 8 from index 1 to index 2, both exclusive.
    """
    result = []
    for i in range(1, 2):
        if nums[i] % 8 != 0:
            result.append(nums[i])
    return result