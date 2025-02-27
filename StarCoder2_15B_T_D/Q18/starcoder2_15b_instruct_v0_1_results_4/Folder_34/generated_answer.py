def sum_ints_div_by_either_nums(nums):
    """
    Returns the sum of all integers divisible by either 9 or 11 from index 60 to index 200, both inclusive.
    If no such integers exist in the specified range, returns 0.
    """
    return sum((num for i, num in enumerate(nums) if i >= 60 and i <= 200 and (num % 9 == 0) or num % 11 == 0))