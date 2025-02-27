def sum_ints_div_by_either_nums(nums):
    """
    Returns the sum of all integers divisible by either 2 or 1 from index 0 to index 1, both inclusive.
    If no such integers exist in the specified range, the function returns 0.
    """
    sum_divisible = 0
    for num in nums:
        if num % 2 == 0 or num % 1 == 0:
            sum_divisible += num
    return sum_divisible