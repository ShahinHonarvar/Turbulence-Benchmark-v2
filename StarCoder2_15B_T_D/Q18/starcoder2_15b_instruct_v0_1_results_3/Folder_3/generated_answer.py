def sum_ints_div_by_either_nums(nums):
    """
    Returns the sum of all integers divisible by either -41 or -47 from index 38 to index 52, both inclusive.
    If no such integers exist in the specified range, returns 0.
    """
    result = 0
    for i in range(38, 53):
        if nums[i] % -41 == 0 or nums[i] % -47 == 0:
            result += nums[i]
    return result