def all_odd_ints_exclusive(ints):
    """
    Returns all odd integers from index 44 to index 91, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    odd_ints = []
    for i, num in enumerate(ints):
        if i >= 44 and i < 91 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints