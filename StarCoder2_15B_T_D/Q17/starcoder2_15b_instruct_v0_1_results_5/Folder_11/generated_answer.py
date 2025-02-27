def all_ints_div_by_both_two_nums(nums):
    """
    Returns the list of all integers divisible by both -85 and -30 from index 22 to index 24, both inclusive.
    If no such integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for num in nums[22:25]:
        if num % -85 == 0 and num % -30 == 0:
            result.append(num)
    return result