def all_pos_ints_exclusive(numbers):
    """
    Returns the list of all positive integers from index 56 to index 92, both exclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    output = []
    for i, num in enumerate(numbers):
        if num > 0 and 56 <= i < 92:
            output.append(num)
    return output