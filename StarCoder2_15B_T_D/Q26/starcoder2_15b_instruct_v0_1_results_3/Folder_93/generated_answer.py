def sum_in_range(numbers):
    """
    Write a function called'sum_in_range' that takes one argument, a list of integers,
    and returns the sum of all integers from the given list that are between -23 and 64,
    both inclusive. If the given list does not contain such integers, the function should
    return 0.
    """
    return sum((n for n in numbers if -23 <= n <= 64))