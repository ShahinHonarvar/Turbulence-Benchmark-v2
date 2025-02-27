def sum_in_range(nums):
    """Return the sum of all integers from the given list that are between 138 and 858, both inclusive. If the given list does not contain such integers, return 0."""
    return sum((num for num in nums if 138 <= num <= 858))