def all_pos_ints_exclusive(numbers):
    """
    Returns the list of all positive integers from index 6 to index 9, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in range(6, 9):
        if numbers[i] > 0:
            result.append(numbers[i])
    return result