def sum_ints_div_by_either_nums(nums):
    """
    Returns the sum of all integers divisible by either 6 or -3 in the specified range.
    """
    sum_divisible = 0
    for i in range(10):
        if nums[i] % 6 == 0 or nums[i] % -3 == 0:
            sum_divisible += nums[i]
    return sum_divisible