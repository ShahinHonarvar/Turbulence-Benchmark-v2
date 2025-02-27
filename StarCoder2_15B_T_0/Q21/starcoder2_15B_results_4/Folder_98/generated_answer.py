def all_ints_div_by_num(nums):
    """
    Returns the list of all integers divisible by 6 from index 0 to index 0, both inclusive.
    If no such integers exist, returns an empty list.
    """
    return [num for num in nums if num % 6 == 0]