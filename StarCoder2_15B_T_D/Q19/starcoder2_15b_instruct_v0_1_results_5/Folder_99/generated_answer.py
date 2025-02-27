def all_ints_not_div_by_num(nums):
    """
    Returns the list of all integers not divisible by 310 from index 387 to index 516, both exclusive.
    If no such integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums[387:516] if num % 310 != 0]