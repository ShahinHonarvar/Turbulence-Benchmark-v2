def sum_in_range(nums):
    """
    Returns the sum of all integers from the given list that are between 138 and 858, both inclusive.
    If the given list does not contain such integers, the function should return 0.
    """
    total = 0
    for num in nums:
        if 138 <= num <= 858:
            total += num
    return total