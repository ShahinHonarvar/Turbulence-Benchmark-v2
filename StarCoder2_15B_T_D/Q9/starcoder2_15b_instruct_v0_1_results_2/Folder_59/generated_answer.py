def all_odd_ints_inclusive(ints):
    """
    Returns a list of all odd integers from index 0 to index 9, both inclusive, if they exist.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    odd_ints = []
    for i, num in enumerate(ints):
        if i >= 0 and i <= 9:
            if num % 2 != 0:
                odd_ints.append(num)
    return odd_ints