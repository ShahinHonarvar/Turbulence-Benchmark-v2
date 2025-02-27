def all_pos_ints_exclusive(numbers):
    """
    Returns the list of all positive integers from index 64 to index 80, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(numbers):
        if num > 0 and 64 <= i < 80:
            result.append(num)
    return result