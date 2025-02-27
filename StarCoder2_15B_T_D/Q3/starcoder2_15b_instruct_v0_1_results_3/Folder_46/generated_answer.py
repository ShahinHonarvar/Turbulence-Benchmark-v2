def all_pos_ints_inclusive(numbers):
    """
    Returns the list of all positive integers from index 30 to index 87, both inclusive.
    If no positive integers exist in the specified range, the function returns an empty list.
    """
    return [num for num in numbers[30:88] if num > 0]