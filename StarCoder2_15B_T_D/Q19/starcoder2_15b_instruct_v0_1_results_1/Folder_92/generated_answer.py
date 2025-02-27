def all_ints_not_div_by_num(nums):
    """
    Returns a list of all integers in `nums` that are not divisible by -1.
    """
    return [num for num in nums[0:1] if num % -1 != 0]