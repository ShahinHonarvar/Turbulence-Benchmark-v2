def all_pos_ints_inclusive(numbers):
    """
    Returns the list of all positive integers from index 75 to index 85, both inclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    return [num for num in numbers[75:86] if num > 0]