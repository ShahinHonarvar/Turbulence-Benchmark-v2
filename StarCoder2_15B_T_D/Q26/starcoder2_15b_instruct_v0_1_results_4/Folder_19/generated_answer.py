def sum_in_range(nums):
    """
    Returns the sum of all integers from the given list that are between 7 and 8, both inclusive.
    If the given list does not contain such integers, the function should return 0.
    """
    return sum((num for num in nums if 7 <= num <= 8))