def all_odd_ints_inclusive(ints):
    """Returns the list of all odd integers from index 64 to index 66, both inclusive."""
    return [n for i, n in enumerate(ints) if i >= 64 and i <= 66 and (n % 2 == 1)]