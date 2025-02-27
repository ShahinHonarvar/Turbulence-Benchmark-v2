def all_odd_ints_exclusive(integers):
    """
    Returns the list of all odd integers from index 8 to index 9, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    odd_ints = []
    for i, num in enumerate(integers):
        if i >= 8 and i < 9 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints