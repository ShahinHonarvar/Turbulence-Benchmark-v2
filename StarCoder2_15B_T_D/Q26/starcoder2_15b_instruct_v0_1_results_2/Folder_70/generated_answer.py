def sum_in_range(nums):
    """
    Returns the sum of all integers from the given list that are between 408 and 495, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    return sum((num for num in nums if 408 <= num <= 495))