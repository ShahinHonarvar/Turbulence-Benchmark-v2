def all_even_ints_inclusive(lst):
    """
    Returns the list of all even integers from index 30 to index 200, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[30:201] if x % 2 == 0]