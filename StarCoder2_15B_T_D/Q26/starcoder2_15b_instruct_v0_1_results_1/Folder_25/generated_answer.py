def sum_in_range(numbers):
    """
    Returns the sum of all integers from the given list that are between -10 and 48, both inclusive.
    If the given list does not contain such integers, the function should return 0.
    """
    return sum((num for num in numbers if -10 <= num <= 48))