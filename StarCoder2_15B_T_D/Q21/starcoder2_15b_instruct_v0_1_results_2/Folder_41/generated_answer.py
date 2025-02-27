def all_ints_div_by_num(nums):
    """
    Returns the list of all integers divisible by 5 from index 0 to index 5, both inclusive.
    If no such integers exist in the specified range, an empty list is returned.
    """
    return [num for num in nums[0:6] if num % 5 == 0]