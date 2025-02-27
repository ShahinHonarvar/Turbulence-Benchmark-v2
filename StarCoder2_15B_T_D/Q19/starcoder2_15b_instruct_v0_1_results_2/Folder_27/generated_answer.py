def all_ints_not_div_by_num(nums):
    """
    Returns the list of all integers not divisible by -93 from index 14 to index 21, both exclusive.
    If no such integers exist in the specified range, the function returns an empty list.
    """
    result = [num for i, num in enumerate(nums) if i >= 14 and i < 21 and (num % -93 != 0)]
    return result