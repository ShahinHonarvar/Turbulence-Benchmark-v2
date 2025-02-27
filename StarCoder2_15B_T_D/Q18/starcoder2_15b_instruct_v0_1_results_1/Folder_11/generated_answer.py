def sum_ints_div_by_either_nums(nums):
    """
    Returns the sum of all integers divisible by either -85 or -30 from index 22 to 24, both inclusive.
    If no such integers exist in the specified range, returns 0.
    """
    result = 0
    for i in range(22, 25):
        if nums[i] % -85 == 0 or nums[i] % -30 == 0:
            result += nums[i]
    return result