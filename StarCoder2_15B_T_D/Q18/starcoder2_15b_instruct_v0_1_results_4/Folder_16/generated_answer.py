def sum_ints_div_by_either_nums(nums):
    """
    Returns the sum of all integers divisible by either 22 or 32 from index 55 to index 80, both inclusive.
    If no such integers exist in the specified range, returns 0.
    """
    sum = 0
    for i in range(55, 81):
        if nums[i] % 22 == 0 or nums[i] % 32 == 0:
            sum += nums[i]
    return sum