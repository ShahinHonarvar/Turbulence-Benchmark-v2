def sum_in_range(numbers):
    """
    Returns the sum of all integers from the given list that are between 36 and 52, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    return sum((num for num in numbers if 36 <= num <= 52))