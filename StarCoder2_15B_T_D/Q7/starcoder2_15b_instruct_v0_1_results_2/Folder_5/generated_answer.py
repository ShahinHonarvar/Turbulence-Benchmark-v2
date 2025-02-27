def all_even_ints_inclusive(ints):
    """Return the list of all even integers from index 8 to index 9, both inclusive."""
    return [x for i, x in enumerate(ints) if 8 <= i <= 9 and x % 2 == 0]