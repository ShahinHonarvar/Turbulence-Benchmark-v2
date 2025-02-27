def sum_in_range(nums):
    """
    Returns the sum of all integers from the given list that are between 5 and 7, both inclusive.
    If the given list does not contain such integers, the function should return 0.
    """
    filtered_nums = list(filter(lambda x: 5 <= x <= 7, nums))
    return sum(filtered_nums) if filtered_nums else 0