def sum_in_range(numbers):
    """
    Returns the sum of all integers from the given list that are between 2 and 6, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    sum_ = 0
    for num in numbers:
        if 2 <= num <= 6:
            sum_ += num
    return sum_