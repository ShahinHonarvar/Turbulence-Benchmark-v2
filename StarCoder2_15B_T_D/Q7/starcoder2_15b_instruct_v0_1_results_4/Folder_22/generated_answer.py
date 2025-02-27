def all_even_ints_inclusive(ints):
    """
    Returns a list of all even integers from index 40 to index 200, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    return [i for i in ints[40:201] if i % 2 == 0]