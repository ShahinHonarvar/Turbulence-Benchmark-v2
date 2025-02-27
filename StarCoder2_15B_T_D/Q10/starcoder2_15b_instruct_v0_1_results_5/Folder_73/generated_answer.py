def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers from index 36 to index 85, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(ints):
        if i >= 36 and i < 85 and (num % 2 == 1):
            result.append(num)
    return result