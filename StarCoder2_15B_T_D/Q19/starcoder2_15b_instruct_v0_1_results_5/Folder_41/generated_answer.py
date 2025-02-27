def all_ints_not_div_by_num(nums):
    """
    Returns a list of all integers not divisible by -3 from index 0 to index 8, both exclusive.
    If no such integers exist, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i < 8 and num % -3 != 0]