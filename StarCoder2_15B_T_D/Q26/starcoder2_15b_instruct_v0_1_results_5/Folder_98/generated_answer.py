def sum_in_range(numbers):
    """
    Returns the sum of all integers in the given list that are between 3 and 8, both inclusive.
    If the given list does not contain such integers, returns 0.
    """
    return sum((num for num in numbers if 3 <= num <= 8))