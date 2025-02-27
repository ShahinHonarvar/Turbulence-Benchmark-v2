def all_pos_ints_exclusive(numbers):
    """
    Returns the list of all positive integers from index 48 to index 74, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [number for number in numbers[48:74] if number > 0]