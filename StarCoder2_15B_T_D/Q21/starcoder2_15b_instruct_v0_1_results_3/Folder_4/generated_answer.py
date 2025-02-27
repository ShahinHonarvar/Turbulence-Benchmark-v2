def all_ints_div_by_num(nums):
    """
    Returns a list of all integers divisible by -14 from index 12 to index 92, both inclusive.
    If no such integers exist, returns an empty list.
    """
    return [num for i, num in enumerate(nums) if i >= 12 and i <= 92 and (num % -14 == 0)]