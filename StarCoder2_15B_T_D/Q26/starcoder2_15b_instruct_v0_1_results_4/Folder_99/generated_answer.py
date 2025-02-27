def sum_in_range(nums):
    """
    Returns the sum of all integers in `nums` that are between 782 and 787, both inclusive.
    If there are no such integers, returns 0.
    """
    total = 0
    for num in nums:
        if 782 <= num <= 787:
            total += num
    return total