def all_ints_div_by_num(nums):
    """
    Returns the list of all integers divisible by 20 from index 31 to index 92, both inclusive.
    If no such integers exist in the specified range, the function returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i >= 31 and i <= 92 and (num % 20 == 0)]