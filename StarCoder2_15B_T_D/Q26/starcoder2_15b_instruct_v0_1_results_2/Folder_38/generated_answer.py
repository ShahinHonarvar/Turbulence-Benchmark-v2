def sum_in_range(numbers):
    """
    Returns the sum of all integers in the given list that are between 44 and 67, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    return sum((num for num in numbers if 44 <= num <= 67))