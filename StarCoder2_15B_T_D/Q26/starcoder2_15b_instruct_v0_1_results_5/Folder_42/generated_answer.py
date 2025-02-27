def sum_in_range(nums):
    """
    Returns the sum of all integers from `nums` that are between 141 and 262, both inclusive.
    If there are no such integers, returns 0.
    """
    return sum((n for n in nums if 141 <= n <= 262))