def all_odd_ints_exclusive(ints):
    """
    Return all odd integers from index 40 to index 200, both exclusive.
    If no odd integers exist in the specified range, return an empty list.
    """
    return [n for i, n in enumerate(ints) if i >= 40 and i < 200 and (n % 2 == 1)]