def sum_in_range(numbers):
    """
    Returns the sum of all integers from the given list
    that are between -616 and -205, both inclusive.
    """
    total = 0
    for num in numbers:
        if -616 <= num <= -205:
            total += num
    return total