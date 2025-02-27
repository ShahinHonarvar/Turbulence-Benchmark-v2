def sum_in_range(nums):
    """
    Returns the sum of all integers from the given list that are between 514 and 816, both inclusive.
    If the given list does not contain such integers, the function should return 0.
    """
    total = 0
    for num in nums:
        if 514 <= num <= 816:
            total += num
    return total