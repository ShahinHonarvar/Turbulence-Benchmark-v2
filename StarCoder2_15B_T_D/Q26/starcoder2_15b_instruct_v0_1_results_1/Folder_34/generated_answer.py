def sum_in_range(nums):
    """
    Returns the sum of all integers in `nums` that are between 4 and 7, both inclusive.
    If there are no such integers, returns 0.
    """
    total = 0
    for num in nums:
        if 4 <= num <= 7:
            total += num
    return total