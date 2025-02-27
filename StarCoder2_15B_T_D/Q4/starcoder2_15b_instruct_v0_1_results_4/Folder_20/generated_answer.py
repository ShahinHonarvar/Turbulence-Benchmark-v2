def all_pos_ints_exclusive(numbers):
    """
    Returns the list of all positive integers from index 59 to index 93, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [num for num in numbers[59:93] if num > 0]