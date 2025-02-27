def sum_in_range(nums):
    """
    Returns the sum of all integers from the given list that are between 3 and 6, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    sum = 0
    for num in nums:
        if 3 <= num <= 6:
            sum += num
    return sum