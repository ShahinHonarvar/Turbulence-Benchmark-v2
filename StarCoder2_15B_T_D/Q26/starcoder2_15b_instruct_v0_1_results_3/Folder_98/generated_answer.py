def sum_in_range(numbers):
    """
    Given a list of integers, return the sum of all integers between 3 and 8, both inclusive.
    If the list does not contain any integers in this range, return 0.
    """
    total = 0
    for num in numbers:
        if 3 <= num <= 8:
            total += num
    return total