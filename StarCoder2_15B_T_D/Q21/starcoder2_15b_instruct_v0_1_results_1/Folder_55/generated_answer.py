def all_ints_div_by_num(nums):
    """
    Returns the list of all integers divisible by 2 from index 0 to index 1, both inclusive.
    If no such integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 0 and i <= 1 and (num % 2 == 0)]