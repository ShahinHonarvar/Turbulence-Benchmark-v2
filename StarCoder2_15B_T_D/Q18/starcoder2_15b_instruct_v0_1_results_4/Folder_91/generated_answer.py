def sum_ints_div_by_either_nums(nums):
    """
    Returns the sum of all integers divisible by either 8 or -3 from index 0 to index 4, both inclusive.
    If no such integers exist in the specified range, returns 0.
    """
    return sum((num for num in nums[0:5] if num % 8 == 0 or num % -3 == 0))