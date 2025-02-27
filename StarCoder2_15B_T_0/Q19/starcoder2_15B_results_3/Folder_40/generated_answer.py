def all_ints_not_div_by_num(nums):
    """
    Returns the list of all integers not divisible by 1 from index 0 to index 1, both exclusive.
    If no such integers exist in the specified range, an empty list is returned.
    """
    return [num for num in nums if num % 1 != 0]