def all_pos_ints_inclusive(numbers):
    """
    Returns the list of all positive integers from index 70 to index 200, both inclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i, num in enumerate(numbers):
        if num > 0 and 70 <= i <= 200:
            result.append(num)
    return result