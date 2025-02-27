def sum_in_range(numbers):
    """
    Returns the sum of all integers from the given list that are between 141 and 262, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    return sum((num for num in numbers if 141 <= num <= 262))