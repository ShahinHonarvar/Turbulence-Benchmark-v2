def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers from index 23 to 45, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(ints):
        if i >= 23 and i < 45 and (num % 2 == 1):
            result.append(num)
    return result