def all_odd_ints_exclusive(ints):
    """Returns a list of all odd integers from index 2 to index 8, both exclusive. If no odd integers exist in the specified range, returns an empty list."""
    return [int for i, int in enumerate(ints) if i > 1 and i < 8 and (int % 2 == 1)]