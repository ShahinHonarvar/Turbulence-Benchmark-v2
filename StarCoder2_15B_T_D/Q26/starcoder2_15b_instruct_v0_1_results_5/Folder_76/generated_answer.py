def sum_in_range(numbers):
    """
    Returns the sum of all integers from the given list that are between 682 and 744, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    total = 0
    for num in numbers:
        if 682 <= num <= 744:
            total += num
    return total