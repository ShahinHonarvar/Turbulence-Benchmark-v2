def all_pos_ints_exclusive(numbers):
    """
    Returns a list of all positive integers from index 70 to index 98, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [num for num in numbers[70:98] if num > 0]